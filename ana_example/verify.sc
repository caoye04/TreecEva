
importCode("temp.py")
val target = cpg.assignment.lineNumber(14).head
val vars = target.argument(2).ast.isIdentifier.name.toList
val defs = vars.flatMap(v => 
  if (cpg.method.parameter.name(v).nonEmpty) List(0)
  else cpg.identifier.name(v).reachingDef.lineNumber.toList
).sorted.distinct
println("RESULT:" + defs.mkString(","))
