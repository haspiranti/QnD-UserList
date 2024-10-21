#!/usr/lib/python3

import io
import argparse

def get_arguments():
	
    parser = argparse.ArgumentParser(description="Mastermind takes command-line arguments or a text file to parse first, middle, and last names into a wordlist for enumeration, fuzzing, and brute forcing.")
    
    exclusive = parser.add_mutually_exclusive_group(required=True)

    exclusive.add_argument("-f", "--file", type=argparse.FileType('r'), help="Input file name")
    exclusive.add_argument("-n", "--name", type=str, help="Input name")
    parser.add_argument("-o", "--output", type=str, default="usernames.txt", help="Output file path")

    args = parser.parse_args()

    if args.output:
        print(f"Output file saving to {args.output}")
    
    if args.file:
        return args.file, args.output
    elif args.name:
        return args.name, args.output


def parse_data(data):
    
    usernames = []

    if isinstance(data, str):
        name_parts = data.split(" ")

        first_name = name_parts[0]
        middle_name = name_parts[1] if len(name_parts) > 2 else ''
        last_name = name_parts[-1] if len(name_parts) > 1 else ''
        first_initial = first_name[0] if first_name else ''
        middle_initial = middle_name[0] if middle_name else ''
        last_initial = last_name[0] if last_name else ''
        
        one_user = create_usernames(first_name, middle_name, last_name, first_initial, middle_initial, last_initial)
    
        for value in one_user.values():
            usernames.append(value)
        
        return usernames


    elif isinstance(data, io.TextIOBase):
        for line in data:
            name_parts = line.split()
            if name_parts:
                first_name = name_parts[0]
                middle_name = name_parts [1] if len(name_parts) > 2 else ''
                last_name = name_parts[-1] if len(name_parts) > 1 else ''
                first_initial = first_name[0] if first_name else ''
                middle_initial = middle_name[0] if middle_name else ''
                last_initial = last_name[0] if last_name else ''

                one_user = create_usernames(first_name, middle_name, last_name, first_initial, middle_initial, last_initial)

                for value in one_user.values():
                    usernames.append(value)

        return usernames
    else:
        print(f"Unknown data type: {type(data)}")
        exit(1)
                

def create_usernames(first_name=None, middle_name=None, last_name=None, first_initial=None, middle_initial=None, last_initial=None):
    username_dict = {
        'fn': first_name,
        'ln': last_name,
        'fnln': f"{first_name}{last_name}",
        'fn.ln': f"{first_name}.{last_name}",
        'filn': f"{first_initial}{last_name}",
        'fi.ln': f"{first_initial}.{last_name}",
        'fnli': f"{first_name}{last_initial}",
        'fn.li': f"{first_name}.{last_initial}",
        #'fili': f"{first_initial}{last_initial}",
        #'fi.li': f"{first_initial}.{last_initial}",
        'lnfn': f"{last_name}{first_name}",
        'ln.fn': f"{last_name}.{first_name}",
        'lnfi': f"{last_name}{first_initial}",
        'ln.fi': f"{last_name}.{first_initial}",
        'lifn': f"{last_initial}{first_name}",
        'li.fn': f"{last_initial}.{first_name}",
        #'lifi': f"{last_initial}{first_initial}",
        #'li.fi': f"{last_initial}.{first_initial}",
        'fimiln': f"{first_initial}{middle_initial}{last_name}" if middle_name else '',
        'fimi.ln': f"{first_initial}{middle_initial}.{last_name}" if middle_name else '',
        'fnmiln': f"{first_name}{middle_initial}{last_name}" if middle_name else '',
        'fn.mi.ln': f"{first_name}.{middle_initial}.{last_name}" if middle_name else '',
        'fnmnln': f"{first_name}{middle_name}{last_name}" if middle_name else '',
        'fn.mn.ln': f"{first_name}.{middle_name}.{last_name}" if middle_name else '',
        'fn-ln': f"{first_name}-{last_name}",
        'fi-ln': f"{first_initial}-{last_name}",
        'fn-li': f"{first_name}-{last_initial}",
        #'fi-li': f"{first_initial}-{last_initial}",
        'ln-fn': f"{last_name}-{first_name}",
        'ln-fi': f"{last_name}-{first_initial}",
        'li-fn': f"{last_initial}-{first_name}",
        #'li-fi': f"{last_initial}-{first_initial}",
        'fimi-ln': f"{first_initial}{middle_initial}-{last_name}" if middle_name else '',
        'fn-mi-ln': f"{first_name}-{middle_initial}-{last_name}" if middle_name else '',
        'fn-mn-ln': f"{first_name}-{middle_name}-{last_name}" if middle_name else '',
        'fn_ln': f"{first_name}_{last_name}",
        'fi_ln': f"{first_initial}_{last_name}",
        'fn_li': f"{first_name}_{last_initial}",
        #'fi_li': f"{first_initial}_{last_initial}",
        'ln_fn': f"{last_name}_{first_name}",
        'ln_fi': f"{last_name}_{first_initial}",
        'li_fn': f"{last_initial}_{first_name}",
        #'li_fi': f"{last_initial}_{first_initial}",
        'fimi_ln': f"{first_initial}{middle_initial}_{last_name}" if middle_name else '',
        'fn_mi_ln': f"{first_name}_{middle_initial}_{last_name}" if middle_name else '',
        'fn_mn_ln': f"{first_name}_{middle_name}_{last_name}" if middle_name else ''
    }
    return username_dict


def write_output(usernames, output):

    with open(output, 'a') as f:
        for line in usernames:
            if line != '':
                f.write(f"{line}\n")


def main():
    
    data, output = get_arguments()
    usernames = parse_data(data)
    
    write_output(usernames, output)


if __name__ == "__main__":
	main()
