
from Autodesk.Revit.DB import Transaction

def inserir_parametro_aninhado(instancias, nomeParametroHospedeiro, nomeParametroIncorporado):

    contador = 0
    for elemento in instancias:
        superComponent = elemento.SuperComponent
        if superComponent:
            elementoAninhado = elemento
            elementoHospedeiro = elemento.SuperComponent

            parametroIncorporado = elementoHospedeiro.LookupParameter(nomeParametroIncorporado)
            if parametroIncorporado:
                valorParametroIncorporado = parametroIncorporado.AsString()

                parametroHospedeiro = elementoAninhado.LookupParameter(nomeParametroHospedeiro)
                if parametroHospedeiro:
                    parametroHospedeiro.Set(valorParametroIncorporado)
                contador += 1

    return contador