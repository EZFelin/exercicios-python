# https://investalk.bb.com.br/noticia/irpf-2024-esta-chegando-a-hora-do-imposto-de-renda-veja-como-declarar-investimentos
# Faça um programa que solicite ao usuário o valor de seus ganhos e calcule o imposto de renda a ser pago de acordo com as seguintes faixas de renda:
# - Até R$ 2.259,20: Isento
# - De R$ 2.259,21 até R$ 2.826,65: Alíquota de 7,5%
# - De R$ 2.826,66 até R$ 3.751, 5: Alíquota de 15%
# - De R$ 3.751,06 até R$ 4.664,68: Alíquota de 22,5%
# - Acima de R$ 4.664,68: Alíquota de 27,5%
vg=float(input("Me informe seu valor de ganhos: "))
if vg<=2259.20:
    print("Não irá ter que pagar")
elif vg>=2259.21 and vg<=2826.65:
    print("Irá ter que pagar aliquota de 7,5%")
elif vg>=2826.66 and vg<=3751.5:
    print("Irá ter que pagar aliquota de  15%")
elif vg>=3751.06 and vg<=4664.68:
    print("Irá ter que pagar aliquota de  22,5%")
elif vg>4664.68:
    print("Irá ter que pagar aliquota de  27,5%")
  


