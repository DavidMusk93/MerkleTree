# MerkleTree
Merkle tree is a classic data structure for checking data integrity, this project aim to build tree and simulate the challenge-respond between client and server.

Let imagine a scenery, you upload a 2GB file `A` to you web server and the file is stroed block by block (a<sub>1</sub>, a<sub>2</sub>, ...). Before you upload `A`, you stroe a `root node` of the merkle tree which is caculated by those blocks. After you upload `A`, you delete file `A` in your computer. After a period, you want to make sure if those blocks are integral. Then, you download one of the blocks from sever (to be simplified, suppose you download a<sub>1</sub>), at the sometime the server returns you a `authentication path`. You get a value caculated by a<sub>1</sub> and `authentication path`, after that, you check in if `root node` is equal to the caculated value, if ture, you get a answer 'Server is good, the data is integrity.', else you wonder 'On, no... the data is not integrity!'.

> ### What is Merkle Tree looks like?

<div align="center">
  <img src="MerkleTree.png" width=100% alt="MerkleTree">
  <p>pic1. Merkle Tree classic construction</p>
</div>

Suppose we split file `A` into 8 equal pieces, this is block<sub>1</sub>, block<sub>2</sub>, ..., block<sub>8</sub>. We use `sha256` to get the blcok hash tags corresponding to X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>8</sub> in pic1. We class nodes as follows:

- leaf node: X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>8</sub>;
- middle node (a.k.a none-leaf node): A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>14</sub>;
- roof node: A<sub>15</sub>.
  
In [merkle_tree.py](merkle.tree.py), the `Node` class is implemented. Each node has five properties:
1. **node_id**: to identify node;
2. **value**: each node maintain a value which is bonded with its child nodes;
3. **parent_node**: let's take A<sub>10</sub> for example, its parent node is A<sub>13</sub>;
4. **left_node**: Merkle Tree is a sequence structure, A<sub>9</sub> is the left child of A<sub>13</sub>;
5. **right_node**: similar to above, A<sub>10</sub> is the right child of A<sub>13</sub>. 

In Merkle Tree, the parent node's value is bonded with its child's values. To be simplified, I choose sha512:
<p align="center">parent_node.value = sha512(right_child.value + left_child.vlaue)</p>

However, before we generate a Merkle Tree, how to get tags X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>8</sub>? As we mentioned above, X<sub>i</sub> is calculated by block<sub>i</sub> using sha256 where i &#8712; (1, 2, ..., 8).

> ### How to split a file into blocks with specified block size?
