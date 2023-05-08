def aprovado(nota1, nota2):
   media = (nota1 + nota2) / 2.0
   if media >= 60.0:
     return True
   else:
     return False

 nota1= float(input('nota do primeiro bimestre: '))
 nota2= float(input('nota do segundo bimestre: '))
 if aprovado(nota1,nota2):
   print('você foi aprovado')
 else:
  print('você ficou em prova final')
