from octoprint_util import keys

def main():
    print(keys.probe('octopi.lan'))
    key = keys.request('octopi.lan')['app_token']
    print(key)
    print(keys.check('octopi.lan',key))

if __name__ == '__main__':
    main()
