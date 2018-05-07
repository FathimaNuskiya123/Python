#--------------------------------------------------------------------------------------------
#       AUTHOR - JUSTIN HUBBARD
#
#       PURPOSE - GO THROUGH A SET DIRECTORY AND STANDARDIZE FILE FORMATS TO PIPE DELIMITED
#

# ONLY INPUTS THE USER NEEDS


#--------------------------------------------------------------------------------------------
import tkinter as tk

def file_standardize(read_dir,write_dir):

    import os, pandas, xlrd

    os.chdir(read_dir)

    read_directory = (os.getcwd())

    read_List =[]
    read_File_List = []
    extension_list = []
    for file in os.listdir(read_directory):
        File_append = os.path.join(read_directory, file)
        read_List.append(File_append)
        read_File_List.append(file)
        File_with_extension = file
        extension = file.split('.')[-1]
        extension_list.append(extension)
    read_Data = pandas.DataFrame(
        {"File_Name":read_List,
         "File":read_File_List,
         "Extension":extension_list})

    # Only keep rows that have a valid extension

    # Beam_Data[['File_Name','File','Extension']] = Beam_Data['File_Name'].str.split('.',expand=True)

    read_Data = read_Data[(read_Data['Extension'] =='xlsx')
                          | (read_Data['Extension'] =='csv')
                          | (read_Data['Extension'] =='tsv')
                          | (read_Data['Extension'] =='dlm')]


    # Change to pipe delimited
    for index, row in read_Data.iterrows():
        File_Name = (read_Data['File_Name'][index])
        Extension = (read_Data['Extension'][index])
        File = (read_Data['File'][index])
        File_no_ext = File.split('.')[0]
        Write_Directory = str('/'.join([write_dir,(str('.'.join([File_no_ext,'dlm'])))]))

        if Extension == 'csv':
            read_in_file = pandas.read_csv(File_Name,delimiter=',')
            save_file_to = read_in_file.to_csv(Write_Directory,header=True,index=False,sep='|')
        elif Extension =='tsv':
            read_in_file = pandas.read_csv(File_Name,delimiter='\t')
            save_file_to = read_in_file.to_csv(Write_Directory,header=True,index=False,sep='|')
        elif Extension =='xlsx':
            read_in_file = pandas.read_excel(File_Name)
            save_file_to = read_in_file.to_csv(Write_Directory,header=True,index=False,sep='|')
        elif Extension =='dlm':
            read_in_file = pandas.read_csv(File_Name,delimiter='|')
            save_file_to = read_in_file.to_csv(Write_Directory,header=True,index=False,sep='|')

def main():
    '''Main entry point of the program: Creates windows and kick
       off the event loop for directory locations'''

    # Make a top level Tk window
    root = tk.Tk()
    root.title("File Standardization GUI - Emergent Business Group")
    # Set up a Label for beam
    dir_Label = tk.Label(text="Enter Read Debt Seller Directory: ")
    dir_Label.pack(side=tk.LEFT,padx=15,pady=15)
    # Make input box for Beam data
    dir_box = tk.Entry(root,width=50)
    dir_box.pack(side=tk.LEFT,padx=15,pady=15)
    # Set up Debt Sale label
    write_Label = tk.Label(text="Enter Write Debt Seller Directory: ")
    write_Label.pack(side=tk.LEFT,padx=15,pady=15)
    # Make an input box for debt sale directory
    write_box = tk.Entry(root,width=50)
    write_box.pack(side=tk.LEFT,padx=15,pady=15)
    # exit button
    exitbutton = tk.Button(text="Exit Application",bg='dark gray', command=quit)
    exitbutton.pack(side='bottom', fill='both',padx=15,pady=15)

    def process_callback(dir_box,write_box):
        ''' Callback that's called when the user presses enter or
            clicks the button. '''

        # need to add in error monitor
        read = dir_box.get()
        write = write_box.get()
        file_standardize(read,write)


    # Make submit button that will loop into the beam function
    btn = tk.Button(root, width=25, bd=3, bg='dark gray', text='Submit Directories')
    btn['command'] = lambda arg1 = dir_box, arg2 = write_box : process_callback(arg1,arg2)
    btn.pack(side=tk.LEFT,padx=15,pady=15)

    dir_box.bind('<Return>', process_callback)
    root.mainloop()

if __name__ == '__main__':
    main()
