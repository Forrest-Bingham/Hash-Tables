class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        


class HashTable:
    """
    --MYHASH--

    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):

        self.capacity = capacity #number of slots
        self.storage = [None] * self.capacity 
        self.count = 0 #number of items
        self.loadfactor = .7 #load factor
        self.desizefactor = .2 #desize load factor

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        h = 14695981039346656037
        for b in str(key).encode():
            h *= 1099511628211
            h ^= b
        return h
    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        #hashes the string
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)

        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #hash index key is the index slot after being hashed
        self.count += 1
        print(self.count, "<-------- Current Count")
        #self.resize()
        index = self.hash_index(key)
        node = self.storage[index]

        print(index, "Index")
        if node is None:
            
            #print(node, "<------ is it None*************")
            self.storage[index] = HashTableEntry(key, value)
            print("Adding value (key, value) ", self.storage[index].key, self.storage[index].value)
            return

        prev = node
        #Sets value to the index in storage

        while node is not None and node.key != key:

            prev = node
            print(prev, "---- Prev")
            node = node.next
            print(node, "----- Next Node")

        if prev.key == key:
            prev.value = value
        
        else:
            print(HashTableEntry(key,value), "New value added")
            prev.next = HashTableEntry(key, value)
            print(prev.next.key, prev.next.value)
            

            # if self.storage[index].next is None:
            #     new = HashTableEntry(key,value)
            #     self.storage[index].next = new
            #     return(new, "Next Node", new.key, new.value)
            
            # self.storage[index] = self.storage[index].next
        #self.storage[index] = HashTableEntry(key, value)
        #print("Adding value (key, value) ", self.storage[index].key, self.storage[index].value)
            #while

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        self.storage[index] = None

        # if there exists data at this node
        # loop through all nodes, until you get a key that matches or node is None
        # prev = None
        # while node is not None and node.key != key:
        #     prev = node
        #     node = node.next
        # # if there is nothing, return warning
        # if node is None:
        #     return "Key is not found"
        # # if key matches, delete the node entirely
        # # if node.key == key:
        # else:
        #     if prev is None:
        #         self.storage[index] = node.next
        #         # node = node.next
        #     else:
        #         prev.next = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        # if self.storage[index] == None:
        #     return None
        # else:
        #     return self.storage[index].value

        node = self.storage[index]

        while node is not None and node.key != key:
            node = node.next
        
        if node is None:
            return None
        else:
            return node.value

    def getDesizeFactor(self):
        desize_load_factor = self.count / self.capacity
        print(desize_load_factor, "Calculated desize factor")
        return desize_load_factor

    
    def desize(self):
        print("*************** DESIZE HAS BEEN CALLED*****************")
        print(self.count, "count")
        print(self.capacity, "capacity")
        print(self.desizefactor, "desize factor")
        desize_load = self.getDesizeFactor()
        print(desize_load)
        if self.desizefactor > desize_load:
            print("Is it reaching here? --------------")
            oldHT = self.storage
            print("old self capacity --->", self.capacity)
            self.capacity = self.capacity // 2
            print("new self capacity --->", self.capacity)
            self.storage = [None] * self.capacity

            for node in oldHT:
                while node:
                    self.put(node.key, node.value)
                    node = node.next
        

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

        # if self.count / self.capacity > loadfactor:
        print("******************RESIZE HAS BEEN CALLED ***********************")
        print(self.count, "< -- self.count", "self.capacity ------->", self.capacity)
        print(self.count/self.capacity)
        print("****************************************************************")
        # if load factor > x
        if self.count / self.capacity > self.loadfactor: 
            oldHT = self.storage
            self.capacity = self.capacity * 2
            self.storage = [None] * self.capacity
        #double the size of hash table

        #create ht with correct capacity

        #rehash whatever is in the old hash table to new hash table.
            for node in oldHT:
                while node:
                    self.put(node.key, node.value)
                    node = node.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
    print("My Test")
    ht2 = HashTable(5)

    print(HashTable.hash_index(ht2, "taco"))
    print(HashTable.hash_index(ht2, "burger"))
    print(HashTable.hash_index(ht2, "chips22"))
    print(HashTable.hash_index(ht2, "cat"))
    print(HashTable.hash_index(ht2, "soda"))
    print(HashTable.hash_index(ht2, "cookies"))
    print(ht2, "--------- HT2")
    
    print(HashTable.put(ht2,"burger", 4), "--- put taco")
    print(HashTable.put(ht2,"cookies", 4))
    print(HashTable.put(ht2, "chips22", 4))
    print(HashTable.put(ht2,"chips", 2))
    print(HashTable.put(ht2,"soda", 1))
    print(HashTable.put(ht2,"cat", 0))
    #print(HashTable.get(ht2, "burger"), "--- Get")
    #print(HashTable.get(ht2, "cookies"), "--- Get")
    #print(HashTable.get(ht2, "chips22"))
    # print(ht2.storage[4].key, "----- Storage")
    # print(ht2.storage[4].next.key)
    # print(ht2.storage[4].next.next.key)
    # ht2.resize()
    print(ht2.capacity, "Capacity ")
    print(ht2.storage)

    """ Hash Table resize Test """

    ht = HashTable(20)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    # ht.put("key-3", "val-3")
    # ht.put("key-4", "val-4")
    # ht.put("key-5", "val-5")
    # ht.put("key-6", "val-6")
    # ht.put("key-7", "val-7")
    # ht.put("key-8", "val-8")
    # ht.put("key-9", "val-9")
    #ht.resize()
    print(ht.storage, "before desize")
    print(ht.capacity, "before desize")
    ht.desize()
    print(ht.storage, "after desize")
    print(ht.capacity, "after desize")
    
