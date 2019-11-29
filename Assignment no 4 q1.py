hasban_family = {
    1 :{
        "first name":"hasban",
        "last name":"malick",
        "age":"19",
        "relation":"me" 
    },
    2 :{
        "first name":"rukhsana",
        "last name":"parven",
        "age":"45",
        "relation":"mother of hasban"
    },
    3 :{
        "first name":"ejaz",
        "last name":"malick",
        "age":"50",
        "relation":"father of hasban" 
    },
    4 :{
        "first name":"ahtesham",
        "last name":"malick",
        "age":"28",
        "relation":"brother"
    }
}
print(hasban_family)
print(hasban_family[1])
hasban_family[1]["qualification"]="enter pass"
hasban_family[1]["high qualification"]="doing civil engineering"
hasban_family[4]["qualification"]="b-teach in civil"
print(hasban_family[1])
print(hasban_family[1]["qualification"])
del hasban_family[1]["high qualification"]
print(hasban_family[1])




