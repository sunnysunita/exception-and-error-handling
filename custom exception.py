class DenominatorZeroError(Exception):
    pass


while True:
    try:
        numerator=int(input("enter numerator: "))
        denominator=int(input("enter denominator: "))
        if denominator==0:
            raise DenominatorZeroError("Denominator should not be zero.")
        ans=numerator/denominator
        print("answer: ",ans)
        break
    except ZeroDivisionError:
        print("denominator should not be zero.")
    except DenominatorZeroError:
        print("Denominator should be except zero.")