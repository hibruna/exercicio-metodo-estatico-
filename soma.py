class Soma:
    @staticmethod
    def soma(vetor_valores):
        if (not isinstance(vetor_valores, list)):
            print('O parametro deve ser um vetor')
            return

        if (len(vetor_valores) < 1):
            print('O parametro deve ter pelo menos 1 valor')
            return

        produto_total = None
        for valor in vetor_valores:
            print('O valor atual é ' + str(valor))
            if (produto_total is None):
                produto_total = valor
                print("Fazendo o processo pela primeira vez, o produto total é = " + str(produto_total))
                continue

            print('Agora já tem valor, vamos somar')
            produto_total = produto_total + valor
            print('O novo produto total é ' + str(produto_total))

        return produto_total
