def getInt():
    try:
        value = int(input('Response: '))
    except:
        print('Invalid Value. Re-Enter.')
        value = getInt()
    finally:
        return value
