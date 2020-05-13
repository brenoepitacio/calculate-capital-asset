#Author: Breno Epitácio 
#Linkedin: https://www.linkedin.com/in/breno-epitácio-506911184
from time import sleep
opc = False
while opc != 11:
    print('==>' * 10, 'Menu Principal', '<==' * 10 ) 
    print(''' 
    Índice de liquidez

    [1] Liquidez corrente:
    [2] Liquidez saca:
    [3] Liquidez imediata:
    [4] Liquidez geral:

    Índices de endividamento

    [5] Imobilização do patrimônio liquido:
    [6] Composição de individamento:
    [7] Participação de capital de terceiros: 
    [8] Nível de desconto de duplicatas:
    [9] Imobilização dos recursos não correntes:
    [10] Endividamento financeiro sobre ativo total:
    [11] Sair do programa:
    ''')
    opc = int(input('Escolha uma das opções: '))
    if opc == 1:
        print('Liquidez corrente: LC ')
        ativo_circulante = float(input('Digite o valor do ativo circulante: '))
        passivo_circulante = float(input('Digite o valor do passivo circulante: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          liquidez_corrente = ativo_circulante / passivo_circulante * 100
          print('Calculando.....')
          sleep(2)
          print('O indicador de liquidez corrente é {:.0f}%'.format(liquidez_corrente))
          print('Quanto maior = melhor')
        elif opc == 'N':
          liquidez_corrente = ativo_circulante / passivo_circulante 
          print('Calculando.....')
          sleep(2)
          print('O indicador de liquidez corrente é {:.2f}'.format(liquidez_corrente))
          print('Quanto maior = melhor') 
    elif opc == 2:
        print('Liquidez seca: LC ')
        ativo_circulante = float(input('Digite o valor do ativo circulante: '))
        estoque = float(input('Digite o valor do estoque: '))
        despesas = float(input('Digite o valor das despesas: '))
        passivo_circulante = float(input('Digite o valor do passivo circulante: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          liquidez_seca = (ativo_circulante - estoque - despesas) / passivo_circulante * 100
          print('Calculando.....')
          sleep(2)
          print('O indicador de liquidez seca é {:.0f}%'.format(liquidez_seca))
          print('Quanto maior = melhor')
        elif opc == 'N':
          liquidez_seca = (ativo_circulante - estoque - despesas) / passivo_circulante
          print('Calculando.....')
          sleep(2)
          print('O indicador de liquidez seca é {}'.format(liquidez_seca))
          print('Quanto maior = melhor')
    elif opc == 3:
        print('Liquidez imediata: LI ')
        disponivel = float(input('Digite valor disponível em caixa: '))
        passivo_circulante = float(input('Digite o valor do passivo circulante: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          liquidez_imediata = disponivel / passivo_circulante * 100
          print('Calculando.....')
          sleep(2)
          print('O indicador de liquidez imediata é {:.0f}%'.format(liquidez_imediata))
          print('Quanto maior = melhor')
        elif opc == 'N':
          liquidez_imediata = disponivel / passivo_circulante
          print('Calculando.....')
          sleep(2)
          print('O indicador de liquidez imediata é {}'.format(liquidez_imediata))
          print('Quanto maior = melhor')
    elif opc == 4:
        print('Liquidez geral: LG')
        ativo_circulante = float(input('Digite o valor do ativo circulante: '))
        realizavel_longo_prazo = float(input('Digite o valor do realizável a longo prazo: '))
        passivo_circulante = float(input('Digite o valor do passivo circulante: '))
        passivo_nao_circulante = float(input('Digite o valor do passivo não circulante: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          liquidez_geral = (ativo_circulante + realizavel_longo_prazo) / (passivo_circulante + passivo_nao_circulante) * 100
          print('Calculando.....')
          sleep(2)
          print('O indicador de liquidez geral é {:.0f}%'.format(liquidez_geral))
          print('Quanto maior = melhor')
        elif opc == 'N':
          liquidez_geral = (ativo_circulante + realizavel_longo_prazo) / (passivo_circulante + passivo_nao_circulante)
          print('Calculando.....')
          sleep(2)
          print('O indicador de liquidez geral é {}'.format(liquidez_geral))
          print('Quanto maior = melhor')
    elif opc == 5:
        print('Imobilização do patrimônio liquido: ILP ')
        ativo_permanente = float(input('Digite seu ativo permanente: '))
        patrimonio_liquido = float(input('Digite seu patrimônio líquido: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          ipl = (ativo_permanente / patrimonio_liquido) * 100
          print('Calculando.....')
          sleep(2)
          print('O cálculo da imobilização do patrimônio liquido é {:.0f}%'.format(ipl))
          print('Quanto menor = melhor')
        elif opc == 'N':
          ipl = (ativo_permanente / patrimonio_liquido) 
          print('Calculando.....')
          sleep(2)
          print('O cálculo da imobilização do patrimônio liquido é {}'.format(ipl))
          print('Quanto menor = melhor')
    elif opc == 6:
        print('Calcular a composição de individamento: CE ')
        passivo_circulante = float(input('Digite o valor do passivo circulante: '))
        exigivel_longo_prazo = float(input('Digite o valor do exigível a longo prazo: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          ce = (passivo_circulante / exigivel_longo_prazo) * 100
          print('Calculando.....')
          sleep(2)
          print('O resultado do calculo da composição de individamento é {:.0f}%'.format(ce))
          print('Quanto menor = melhor')
        elif opc == 'N':
          ce = (passivo_circulante / exigivel_longo_prazo)
          print('Calculando.....')
          sleep(2)
          print('O resultado do calculo da composição de individamento é {}'.format(ce))
          print('Quanto menor = melhor')
    elif opc == 7:
        print('Participação do capital de terceiro: PCT ')
        passivo_circulante = float(input('Digite o valor do passivo circulante: '))
        exigivel_longo_prazo = float(input('Digite o valor do exigível a longo prazo: '))
        patrimonio_liquido = float(input('Digite o valor do patrimônio líquido: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          pct = (passivo_circulante + exigivel_longo_prazo) / patrimonio_liquido * 100
          print('Calculando.....')
          sleep(2)
          print('O resultado do calculo de participação do capital de terceiro é {:.0f}%'.format(pct))
          print('Quanto menor = melhor')
        elif opc == 'N':
          pct = (passivo_circulante + exigivel_longo_prazo) / patrimonio_liquido 
          print('Calculando.....')
          sleep(2)
          print('O resultado do calculo de participação do capital de terceiro é {}'.format(pct))
          print('Quanto menor = melhor')
    elif opc == 8:
        print('Nível de desconto de duplicatas: NDD ')
        duplicatas_descontadas = float(input('Digite o valor das duplicatas descontadas: '))
        duplicatas_receber = float(input('Digite o valor das duplicatas a receber: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          ndd = (duplicatas_descontadas / duplicatas_receber) * 100
          print('Calculando.....')
          sleep(2)
          print('O resultado do calculo de nível de desconto de duplicadas é {:.0f}%'.format(ndd))
          print('Quanto menor = melhor')
        elif opc == 'N':
          ndd = (duplicatas_descontadas / duplicatas_receber)
          print('Calculando.....')
          sleep(2)
          print('O resultado do calculo de nível de desconto de duplicadas é {}'.format(ndd))
          print('Quanto menor = melhor')
    elif opc == 9:
        print('Imobilização de recursos não corrente: INRC')
        ativo_permanente = float(input('Digite o valor do ativo permanente: '))
        patrimonio_liquido = float(input('Digite o valor do patrimônio líquido: '))
        exigivel_longo_prazo = float(input('Digite o valor do exigível a longo prazo: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          inrc = ativo_permanente / (patrimonio_liquido + exigivel_longo_prazo) * 100
          print('Calculando.....')
          sleep(2)
          print('O resultado do calculo de imobilização de recursos não corrente foi: {:.0f}%'.format(inrc))
          print('Quanto menor = melhor')
        elif opc == 'N':
          inrc = ativo_permanente / (patrimonio_liquido + exigivel_longo_prazo)
          print('Calculando.....')
          sleep(2)
          print('O resultado do calculo de imobilização de recursos não corrente foi: {}'.format(inrc))
          print('Quanto menor = melhor')
    elif opc == 10:
        print('Endividamento financeiro sobre ativo total: EFSAT')
        duplicatas_descontadas = float(input('Digite o valor das duplicatas descontadas: '))
        instituicoes_financeiras = float(input('Digite o valor da instituição financeiras: '))
        transferencia_longo_prazo = float(input('Digite o valor da transferências de longo prazo: '))
        outros_nao_ciclicos = float(input('Digite o valor dos outros não cíclicos: = dividendo, imposto de renda e outros: ')) 
        exigivel_longo_prazo = float(input('Digite o valor do exigível a longo prazo: '))
        ativo_total = float(input('Digite o valor do ativo total: '))
        opc = str(input('Com porcentagens? S/N: ')).upper()
        if opc == 'S':
          efsat = (duplicatas_descontadas + instituicoes_financeiras + transferencia_longo_prazo + outros_nao_ciclicos + exigivel_longo_prazo) / ativo_total * 100
          print('Calculando.....')
          print('O resultado do calculo do individamento financeiro sobre ativo total é {:.0f}%'.format(efsat))
          print('Quanto menor = melhor')
        elif opc == 'N':
          efsat = (duplicatas_descontadas + instituicoes_financeiras + transferencia_longo_prazo + outros_nao_ciclicos + exigivel_longo_prazo) / ativo_total
          print('Calculando.....')
          print('O resultado do calculo do individamento financeiro sobre ativo total é {}'.format(efsat))
          print('Quanto menor = melhor')
    elif opc == 11:
        sleep(3)
        print('Finalizando programa....')
        sleep(3)
        break
    else:
        print('Opção inválida!')
print('Fim do programa')