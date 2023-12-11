def display_person(**k):
    for key,value in k.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")