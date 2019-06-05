import re # Importamos el modulo regex

# coding: utf-8
global listValues
global symbols
global states
global data
listValues = []
symbols = []
states = 0
data = []
global transitions
transitions = []
global expresion
expresion = ''

def read_file(name):
    try:
        x = open(name, 'r')
        return x
    except:
        return('Something went wrong when reading to the file')
        x.close()

def set_values(values):
    for v in values:
        listValues.append(v)

def get_symbol(v, index):
    i = 0
    if(v.isdigit()):
        for n in listValues:
            if(i == index):
                return n
            i += 1    
    return None

def get_initial(v):
    if (v.isdigit()):
        return int(v)
    else:
        return None

def set_data(values):
    inital_state = values[0:1]
    end_state = values[2: len(values)-1]
    index = 1
    for v in end_state:
        index += 1
        data_state = []
        if len(v) > 0:
            data_state.append(int(inital_state))
            if(get_symbol(v, index)):
                data_state.append(get_symbol(v, index))
                data_state.append(get_initial(v))
        if(len(data_state) == 3):
            data.append(data_state)

def reorder(transitions, symbols):
    a=[]
    states=get_states()
    count=0
    while count <= states:
        b=[]
        for symbol in symbols:
            c=[]
            for transition  in transitions:
                if symbol == transition[1] and count == transition[0]:
                    c.append(transition[2])
            b.append(c)
        a.append(b)
        count+=1
    return a

def get_data():
    try:
        f = read_file('data.csv')
        index = 0
        for linea in f:
            if len(linea) > 1:
                if(index == 0 ):
                    set_values(linea)
                else:
                    set_data(linea)
            index += 1
        transitions = reorder(remove_duplicates(data), get_symbols())
        f.close()
        return transitions
    except Exception as inst:
        raise Exception(inst)
    finally:
        f.close()

def get_symbols():
    try:
        f = read_file('data.csv')
        for idx, linea in enumerate(f):
            if idx == 0:
                for idy, v in enumerate(linea):
                    if idy > 1 and idy%2 == 0 :
                        symbols.append(v)
        f.close()
        return symbols
    except Exception as inst:
        raise Exception(inst)
    finally:
        f.close()

def get_states():
    try:
        f = read_file('data.csv')
        idx=-0
        for linea in f:
            idx+=1
        f.close()
        return idx-2
    except Exception as inst:
        raise Exception(inst)
    finally:
        f.close()

def remove_duplicates(lt):
    new_k = []
    for elem in lt:
        if elem not in new_k:
            new_k.append(elem)
    k = new_k
    return new_k

def automaton(word, current, transitions, symbols,resultado=None):
    if len(word)>0:
        for char in word:
            if not char in symbols:
                return None

        for next in transitions[current][symbols.index(word[0])]:
            current = next
            if len(word) == 1:
                if current == get_states():
                    resultado = True
                else:
                    continue
            else:
                resultado = automaton(word[1:],current, transitions, symbols, resultado)                   
    return resultado
        
def main():
    while(True):
        print('\n<<<===== Choose option =====>>>\n1.Automaton\n2.Exit')
        op = input()
        if op == 1:
            try:
                txt = read_file('data.txt')
                transitions = get_data() 
                # print(transitions, symbols)
                for idx, word in enumerate(txt):
                    if(automaton(word.split('\n')[0],0,transitions, symbols) == True):
                        # print('Valid word')
                        pass
                    else:
                        print('Invalid word line: '+ str(idx))
                txt.close()
            except Exception as e:
                print(e)
            finally:
                txt.close()
        if op == 2:
            break
main()

