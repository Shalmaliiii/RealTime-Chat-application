# **Real Time Chat application (using socket programming)**

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while another socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.
<br /><br />
This Chat Room makes use of TCP protocol that enables users to exchange messages over a network. Before sending packets, TCP establishes the connection between server and client to ensure successful transmission of data. 
It guarantees that the packets will reach the destination without any duplication of data.<br />Therefore TCP is more reliable as it ensures that all segments are received in order and any lost segments are retransmitted. 

---

### Features :
1. Applied multithreading concepts to create a server that can keep track of all threads or clients that connect to it. 
2. Admins can access the room only through password. As storing plain text password is not secure, the password entered by the client is checked by hashing it with the salt of encrypted right_password iterated over 20 times (hash function : SHA1).    
   Hence the rainbow table attacks won’t be effective, as the probability that rainbow table contains hash of common passwords is meager.
3. (Only) Admins can kick and ban users from server.
4. If passcode for Admin is wrong after 3 tries, a temperory alias is generated for the user.

### Example :
- General view of the chat room with 4 clients(threads) : 

![](/images/1..png)

- Wrong password for admin after 3 tries : 

![](/images/2..png)

- Correct password for admin :

![](/images/3..png)

- Kicking a user from the server : 

![](/images/4..png)

- Banning a user from the server :

![](/images/5..png)

- How does a server look like? :

![](/images/6..png)


