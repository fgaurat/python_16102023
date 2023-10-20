from TodoDAO import TodoDAO
import argparse
import configparser
import os
import sys

def main():
    parser = argparse.ArgumentParser(prog='Todos reader',description='Retrieve all todos from DB',epilog='Text at the bottom of help')
    parser.add_argument('config_file',help="Config file")    
    args = parser.parse_args()
    if not os.path.exists(args.config_file):
        print('Fichier de configuration non trouvé',file=sys.stderr)
        sys.exit(-1)

    config = configparser.ConfigParser()
    config.read(args.config_file)

    print(config['DB']['db_file'])
    db_file = config['DB']['db_file']
    dao = TodoDAO(db_file)
    todos = dao.find_all()
    next(todos)
    print(next(todos))

    
def main_args():
    parser = argparse.ArgumentParser(prog='Todos reader',description='Retrieve all todos from DB',epilog='Text at the bottom of help')
    parser.add_argument('db_file',help="DB file")    
    args = parser.parse_args()
    
    if not os.path.exists(args.db_file):
        print('Fichier non trouvé',file=sys.stderr)
        sys.exit(-1)

    dao = TodoDAO(args.db_file)
    todos = dao.find_all()
    next(todos)
    print(next(todos))


if __name__ == '__main__':
    main()