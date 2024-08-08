
from Autodesk.Revit.DB import Transaction

def inserir_parametro_aninhado(instancias, nomeParametroHospedeiro, nomeParametroAninhado):

    contador = 0
    for elemento in instancias:
        superComponent = elemento.SuperComponent
        if superComponent:
            elementoAninhado = elemento
            elementoHospedeiro = elemento.SuperComponent

            parametroHospedeiro = elementoHospedeiro.LookupParameter(nomeParametroHospedeiro)
            if parametroHospedeiro:
                valorParametroHospedeiro = parametroHospedeiro.asString()

                parametroAninhado = elementoAninhado.LookupParameter(nomeParametroAninhado)
                if parametroAninhado:
                    parametroAninhado.Set(valorParametroHospedeiro)
                contador += 1

    return contador