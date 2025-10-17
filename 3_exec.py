# 3_exec.py : demonstration of exec

def run():
    while True:
        s = input('input code: ')
        if s.lower() == 'break': break
        try: exec(s)
        except: print('something went wrong')
    print('run terminated')

if __name__ == '__main__':
    run()