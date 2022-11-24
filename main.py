import Graph
import search

def main(name1,name2):
    name1 = name1.replace(" ", "_")
    name2 = name2.replace(" ", "_")
    link1 = "https://en.wikipedia.org/wiki/" + name1
    link2 = "https://en.wikipedia.org/wiki/" + name2
    p2 = ((name2,link2),None )
    result = Graph.createGraph(search.get_links(link1),p2)
    if result[1]:
        print("     |")
        print("     V")
        print("|"+p2[0][0]+"|")
        print(" ")
        print("*-*-*|Están conectados :D|*-*-*")
    else:
        print("   X")
        print("   X")
        print(" ")
        print("*-*-*|No están conectados :c|*-*-*")

url1 = input("Introduzca el nombre de la primera persona: ")
url2 = input("Introduzca el nombre de la segunda persona: ")
main(url1,url2)
