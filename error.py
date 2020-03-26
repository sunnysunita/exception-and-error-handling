while True:
    try:
        numerator=int(input("enter numerator: "))
        denominator=int(input("enter denominator: "))
        ans=numerator/denominator
        print("answer: ",ans)
        break
    except ZeroDivisionError:
        print("\t\t\tWARNING!!")
        print("::denominator should not be equal to zero!!!::")
        print("enter value again.")
    except ValueError:
        print("\t\t\tWARNING!!")
        print("values should be integer.")
        print("enter value again.")