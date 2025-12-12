# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import parmed as pmd

def mddb():# Carica topologia (prmtop) e coordinate (inpcrd / rst7)
    amber = pmd.load_file('system.prmtop', 'system.inpcrd')

    # (Opzionale) controlla qualche info
    print(amber)
    print("Numero di atomi:", len(amber.atoms))
    print("Box (se presente):", amber.box)

    # Salva in formato GROMACS:
    # .top = topologia, .gro = coordinate + box
    amber.save('system.top', format='gromacs', overwrite=True)
    amber.save('system.gro', overwrite=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mddb()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
