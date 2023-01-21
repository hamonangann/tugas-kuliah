import string
from heapq import heappop, heappush
import copy
from typing import Generator


def set_print(new_print):
    global print
    print = new_print

class Graph:
    def __init__(self):
        self.outdegree: dict[str, list[str]] = {}

    def add_vertex(self, name: str):
        self.outdegree[name] = []

    def clear_edge(self, name: str):
        self.outdegree[name].clear()

    def add_edge(self, from_: str, to: str):
        self.outdegree[from_].append(to)

    def get_neighbours(self, node: str):
        return self.outdegree[node]

    def delete_edge(self, from_: str, to: str, permissive=False):
        self.outdegree[from_].remove(to)

    def delete_node(self, node: str):
        neighbours = self.get_neighbours(node).copy()
        for neighbour in neighbours:
            self.delete_edge(node, neighbour)

    def reverse_direction(self):
        ret = Graph()
        for node in self.outdegree:
            ret.add_vertex(node)

        for node in self.outdegree:
            neighbours = self.get_neighbours(node)
            for neighbour in neighbours:
                ret.add_edge(neighbour, node)
        return ret

    def get_nodes(self):
        return self.outdegree.keys()

    def __contains__(self, item):
        return item in self.outdegree


class Main():
    ALLOWED_MATKUL_NAME_CHARACTERS =  set(string.ascii_letters + "_")

    def __init__(self):
        self.matkul = Graph()

    def run(self):
        while (inp := input("")) != "EXIT":
            command, *arg = inp.split()

            if command == "ADD_MATKUL":
                nama, *prasyarat = arg
                self.add_new_matkul(nama, prasyarat)
            elif command == "EDIT_MATKUL":
                nama, *prasyarat = arg
                self.edit_prasyarat(nama, prasyarat)
            elif command == "CETAK_URUTAN":
                self.cetak_urutan_pengambilan()
            else:
                print("Perintah tidak ditemukan")


    def add_new_matkul(self, nama, matkul_prasyarat):
        if nama in self.matkul:
            print(f"Matkul {nama} sudah ada")
            return

        for prasyarat in matkul_prasyarat:
            if prasyarat not in self.matkul:
                print(f"Matkul {prasyarat} tidak ditemukan")
                return
        self.matkul.add_vertex(nama)
        for prasyarat in matkul_prasyarat:
            self.matkul.add_edge(nama, prasyarat)

    def edit_prasyarat(self, nama, matkul_prasyarat):
        if nama not in self.matkul:
            print(f"Matkul {nama} tidak ditemukan")
            return

        for prasyarat in matkul_prasyarat:
            if prasyarat not in self.matkul:
                print(f"Matkul {prasyarat} tidak ditemukan")
                return

        self.matkul.clear_edge(nama)
        for prasyarat in matkul_prasyarat:
            self.matkul.add_edge(nama, prasyarat)

    def cetak_urutan_pengambilan(self):
        topological = SortedTopological(self.matkul)
        urutan = topological.get_urutan()
        print(", ".join(urutan))


class SortedTopological:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.urutan_pengambilan = []
        self.depth = {nama: -1 for nama in self.graph.outdegree}

    def get_urutan(self):
        for nama in self.graph.outdegree:
            self.dfs(nama)

        heap = []
        for nama, depth in self.depth.items():
            heappush(heap, (depth, nama))
        while heap:
            depth, matkul = heappop(heap)
            self.urutan_pengambilan.append(matkul)

        return self.urutan_pengambilan

    def dfs(self, nama: str):
        if self.depth[nama] != -1:
            return self.depth[nama]
        neighbours = self.graph.get_neighbours(nama)

        max_urutan = 0
        for neighbour in neighbours:
            max_urutan = max(max_urutan, self.dfs(neighbour))
        self.depth[nama] = max_urutan + 1
        return max_urutan + 1




if __name__ == "__main__":

    main = Main()
    main.run()
