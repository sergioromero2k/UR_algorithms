#!/usr/bin/env python3

def main() -> None:
    """ Read number of team members"""
    try:
        entrance = input()
        if not entrance:
            return
        entrance = int(entrance)
        members = []

        if 1 <= entrance <= 100:
            for _ in range(entrance):
                info = input().split()
                if len(info) == 2:
                    name = info[0]
                    age = info[1]
                    if not (age or name):
                        raise Exception("Introduce the age and name.")
                    age = int(age)
                    if 0 <= age <= 100:
                        members.append((name, age))
                    else:
                        raise Exception("Age must be between 0 and 100.")
                else:
                    raise Exception("Only must accept two parameters")
            # Person with maximum age becomes the leader.
            leader = max(members, key=lambda member: member[1])
            leader_name = leader[0]
            number_of_members = entrance - 1
            if number_of_members == 1:
                print(
                    f"Bienvenido equipo de {leader_name} "
                    "compuesto por 1 persona"
                )
            else:
                print(
                    f"Bienvenido equipo de {leader_name} "
                    f"compuesto por {number_of_members} personas"
                )

        else:
            raise Exception("Entrada must be between 0 and 100.")
    except ValueError as e:
        print("Error Value: ", e)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
