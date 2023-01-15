import maps
import search

def main():
    # Run the search
    search.searchGoogle()
    glocations = search.google.locations
    gnames = search.google.names
    center = search.usrLoc

    # generate the map and points
    maps.generate_map(glocations, gnames, center)

    # display the map
    maps.show_map()


if __name__ == '__main__':
    main()
