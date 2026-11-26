
def calculate_fee(category, participants):
    fees = {
        "student": 100,
        "faculty": 200,
        "industry": 500
    }

    if category.lower() not in fees:
        raise ValueError("Invalid registration category")

    return fees[category.lower()] * participants


def participant_details(name, category, participants):
    total = calculate_fee(category, participants)

    print("\nParticipant Details")
    print("Name:", name)
    print("Category:", category)
    print("Number of Participants:", participants)
    print("Total Registration Amount: Rs.", total)

    return total


if __name__ == "__main__":
    name = input("Enter Participant Name: ")
    category = input("Enter Registration Category (Student/Faculty/Industry): ")
    participants = int(input("Enter Number of Participants: "))

    participant_details(name, category, participants)
