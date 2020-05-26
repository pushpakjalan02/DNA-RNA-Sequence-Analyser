def getInt():
    try:
        value = int(input())
    except:
        print('Invalid Value. Re-Enter.')
        value = getInt()
    finally:
        return value
