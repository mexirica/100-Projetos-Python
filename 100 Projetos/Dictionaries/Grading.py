notas={
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

passou={}

def graduado(notas):
    for key,value in notas.items():
        if value>91:
            passou[key]="Excelente"
        elif value>=81 and value<90:
            passou[key]="Excedeu as expectativas"
        elif value>=71 and value<80:
            passou[key]="Aceitável"
        elif value<=70:
            passou[key]="Falhou"
    print(passou)

graduado(notas)