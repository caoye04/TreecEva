# generate_cot_from_trace.py

import json
import os
import re
from openai import OpenAI
from config import API_CONFIG, DATA_DIR


class CoTGenerator:
    def __init__(self):
        self.client = OpenAI(
            api_key=API_CONFIG['api_key'],
            base_url=API_CONFIG['base_url']
        )
        self.model = API_CONFIG['model']
    
    def load_case_data(self, case_file: str, trace_file: str) -> tuple:
        """Load case JSON and execution trace data."""
        case_path = os.path.join(DATA_DIR, case_file)
        trace_path = os.path.join(DATA_DIR, trace_file)
        
        with open(case_path, 'r', encoding='utf-8') as f:
            case_data = json.load(f)
        
        with open(trace_path, 'r', encoding='utf-8') as f:
            trace_data = f.read()
        
        return case_data, trace_data
    
    def parse_trace_info(self, trace_data: str) -> dict:
        """Extract key information from execution trace."""
        lines = trace_data.strip().split('\n')
        
        trace_info = {
            'execution_steps': [],
            'variable_changes': {},
            'final_state': None
        }
        
        for line in lines:
            parts = line.split('\t')
            if len(parts) >= 3:
                line_num = parts[0].strip()
                code_line = parts[1].strip() if len(parts) > 1 else ""
                var_info = parts[2].strip() if len(parts) > 2 else ""
                
                trace_info['execution_steps'].append({
                    'line': line_num,
                    'code': code_line,
                    'variables': var_info
                })
        
        if trace_info['execution_steps']:
            trace_info['final_state'] = trace_info['execution_steps'][-1]
        
        return trace_info
    
    def generate_cot_prompt(self, case_data: dict, trace_data: str) -> str:
        """Generate the prompt for CoT generation."""
        
        task_desc = case_data['task']['description']
        code = case_data['task']['code']
        answer = case_data['task']['answer']
        language = case_data['metadata']['language']
        
        prompt = f"""You are an expert in program analysis and static reasoning. Generate a high signal-to-noise ratio Chain-of-Thought (CoT) that explains how to derive the target answer through backward reasoning from execution traces.

        ## Task Information
        **Language**: {language}
        **Description**: {task_desc}
        **Expected Answer**: {answer}

        ## Code
        ```{language}
        {code}
        ```
        ## Execution Trace
        ```
        {trace_data}
        ```
        Requirements
Generate a backward reasoning chain following this EXACT format:

Start with the target : Identify the final variable and its value
Format:Target: variable_name@LineNumber = value

Backward trace : List execution steps in REVERSE chronological order

Number each step (1, 2, 3, ...)
Include line numbers (L##)
Show variable state changes with arrows (old→new)
Explain conditions and branching decisions
Track dependencies and data flow
Critical dependencies : Summarize key logic

What determines the final result?
What are the control flow conditions?
What is the execution order?
Any important state transformations?
Example Format:
Target: result@L50 = 5

Backward trace:

L45: return total → total@L45 = 5
L42: total += value (2nd addition) → total: 3→5
L40: value = compute(x) → value = 2
L35: total += value (1st addition) → total: 0→3
L33: value = compute(y) → value = 3
...
Critical dependencies:

Final value depends on: two additions
Computation order: y processed before x
Initial state: total = 0
Important:
Use precise line numbers from the trace
Show ALL intermediate steps
Explain WHY each step happens (conditions, loops, etc.)
Use concise technical language
End with: "Thus, variable_name@LineNumber = value"
Generate the CoT now. Output ONLY the CoT text, no JSON wrapper needed."""
        return prompt
    def call_llm(self, prompt):
        """Call LLM API to generate CoT."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in static program analysis and execution trace interpretation. You generate precise, high signal-to-noise ratio reasoning chains."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=4096
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error calling LLM API: {e}")
            return None
    
    def extract_cot_from_response(self, response):
        """Extract CoT from LLM response."""
        try:
            # Remove any JSON code blocks if present
            json_block_match = re.search(r'```json\s*\{[\s\S]*?"cot"\s*:\s*"([\s\S]*?)"\s*\}[\s\S]*?```', response)
            if json_block_match:
                return json_block_match.group(1).replace('\\n', '\n')
            
            # Remove markdown code blocks
            response = re.sub(r'```[a-z]*\n', '', response)
            response = re.sub(r'```', '', response)
            
            # Try to extract JSON object
            json_match = re.search(r'\{\s*"cot"\s*:\s*"([\s\S]*?)"\s*\}', response)
            if json_match:
                return json_match.group(1).replace('\\n', '\n')
            
            # If response starts with "Target:", assume it's already the CoT
            if response.strip().startswith('Target:'):
                return response.strip()
            
            # Fallback: return cleaned response
            return response.strip()
            
        except Exception as e:
            print(f"Error extracting CoT: {e}")
            return response.strip()

    def generate_cot(self, case_file, trace_file, output_file=None):
        """Main function to generate CoT for a case."""
        print(f"Loading data from {case_file} and {trace_file}...")
        case_data, trace_data = self.load_case_data(case_file, trace_file)
        
        print("Generating CoT prompt...")
        prompt = self.generate_cot_prompt(case_data, trace_data)
        
        print("Calling LLM to generate CoT...")
        response = self.call_llm(prompt)
        
        if response is None:
            print("Failed to generate CoT")
            return None
        
        print("Extracting CoT from response...")
        cot = self.extract_cot_from_response(response)
        
        # Update case data with generated CoT
        case_data['task']['cot'] = cot
        
        # Save updated case data
        if output_file:
            output_path = os.path.join(DATA_DIR, output_file)
        else:
            output_path = os.path.join(DATA_DIR, case_file.replace('.json', '_with_cot.json'))
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(case_data, f, indent=2, ensure_ascii=False)
        
        print(f"CoT saved to {output_path}")
        print("\n=== Generated CoT ===")
        print(cot)
        print("=" * 50)
        
        return cot
    
    def batch_generate(self, case_trace_pairs):
        """Generate CoT for multiple cases."""
        results = []
        
        for case_file, trace_file in case_trace_pairs:
            print(f"\n{'='*60}")
            print(f"Processing: {case_file}")
            print(f"{'='*60}")
            
            try:
                cot = self.generate_cot(case_file, trace_file)
                results.append({
                    'case': case_file,
                    'status': 'success',
                    'cot': cot
                })
            except Exception as e:
                print(f"Error processing {case_file}: {e}")
                results.append({
                    'case': case_file,
                    'status': 'error',
                    'error': str(e)
                })
        
        return results

def main():
    """Example usage."""
    generator = CoTGenerator()
    
    # Single case generation
    # print("Generating CoT for case1...")
    # generator.generate_cot('case1.json', 'trace_var_1.txt')
    
    print("\n" + "="*60)
    print("Generating CoT for case2...")
    generator.generate_cot('case2.json', 'trace_var_2.txt')
    
    # Batch generation example (uncomment to use)
    # case_pairs = [
    #     ('case1.json', 'trace_var_1.txt'),
    #     ('case2.json', 'trace_var_2.txt'),
    # ]
    # results = generator.batch_generate(case_pairs)
    # print("\nBatch generation completed:")
    # for result in results:
    #     print(f"  {result['case']}: {result['status']}")


if __name__ == "__main__":
    main()