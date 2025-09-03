

products_content = ""

with open("data/products.csv", "r", encoding="utf-8") as f: 
    lines = f.readlines()
    header = lines[0]
    columns = header.strip("\n").split(",")
    
    items = list()
    
    for row in lines[1:]:
        row_values =  row.strip("\n").split(",")
        row_item = dict() 
        
        i = 0
        for header_column in columns: 
            row_item[header_column] = row_values[i]
            i += 1
        
        print(row_item)
        
    print(lines, columns)
    