o
    ��b�  �                   @   s�   d dl Z d dlZd dl Z d dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZ	dZ
dZdZd	Zd
Ze �d� dd� Zdd� Zdd� Zdd� Zz	e�  e�  W dS  eyf   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s"   t �d� t �d� t �d� d S )N�lolcat banner.sh�.Text�lolcat MyText.txt)�os�system�chdir� r	   r	   �
circle1.py�header(   s   

r   c                   C   s,   t �d� t �d� t �d� t �d� d S )N�..r   r   r   )r   r   r   r	   r	   r	   r
   �header2-   s   


r   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr	   r	   r
   �	logoprint3   s
   
�r   c                  C   sP  	 t �d� tttd t ��} | dkr8t �d� t�  ttd � t�	d� t �
d� t �
d	� t �d
� d S | dkr`t �d� t�  ttd � t�	d� t �
d� t �
d� t �d� d S | dkr�t �d� t�  ttd � t�	d� t �
d� t �
d� t �d� d S | dkr�t �d� t�  ttd � t�	d� t �
d� t �
d� t �d� d S | dkr�t �d� t�  ttd � t�	d� t �
d� t �
d� t �d� d S | dk�rt �d� t�  ttd � t�	d� t �
d� t �
d� t �d� d S | dk�r*t �d� t�  ttd  � t�	d� t �
d� t �
d!� t �d"� d S | d#k�rSt �d� t�  ttd$ � t�	d� t �
d� t �
d%� t �d&� d S | d'k�r|t �d� t�  ttd( � t�	d� t �
d� t �
d)� t �d*� d S | d+k�r�t �d� t�  ttd, � t�	d� t �d-� d S | d.k�r�t �d� t�  ttd/ � t�	d� t �
d� t �
d0� t �
d1� t �d2� d S | d3k�r�t �d� t�  ttd4 � t�	d� t �
d� t �
d0� t �
d5� t �d6� d S | d7k�r%t �d� t�  ttd8 � t�	d� t �
d� t �
d0� t �
d9� t �d:� d S | d;k�rNt �d� t�  ttd< � t�	d� t �
d� t �
d=� t �d>� d S | d?k�rwt �d� t�  ttd@ � t�	d� t �
d� t �
d=� t �dA� d S | dBk�r�t �d� t�  ttd, � t�	d� t �d-� d S | dCk�r�t �d� t�  ttd, � t�	d� t �d-� d S | dDk�r�t �d� t�  ttd, � t�	d� t �d-� d S | dEk�r�t �d� t�  ttd, � t�	d� t �d-� d S | dFk�rt �d� t�  ttdG � t�	d� t �
d� t �
dH� t �dI� d S ttdJ � t�	dK� q)LNTzlolcat option.shz     Choose a Option: �1r   z>

    You Choosed Circle API Key Genarate.

    Please wait...�   r   z.apiGenaratezpython api.py�2zA

    You Choosed Circle ID To Number Option.

    Please wait...z.iDtoNumzpython idtonum.py�3z>

    You Choosed Number To Circle Option.

    Please wait...z.numToIDzpython numToId.py�4zA

    You Choosed Chek Following List Option.

    Please wait...z.showFollowingszpython followings.py�5zA

    You Choosed Chek Followers List Option.

    Please wait...z.showFollowerszpython followers.py�6zB

    You Choosed Clean Following List Option.

    Please wait...z.followingCleanzpython clean.py�7zA

    You Choosed Clean Follower List Option.

    Please wait...z.followerCleanzpython follower.py�8z3

    You Choosed CPoke Option.

    Please wait...z.pokezpython cp.py�9z2

    You Choosed CCOM Option.

    Please wait...z.comzpython cm.pyZ10z!

    You Choosed a premium toolsz*xdg-open https://www.facebook.com/Aru.Ofc/Z11z;

    You Choosed Change Gender Option.

    Please wait...z.changez.genderzpython g.pyZ12z=

    You Choosed Change Birthday Option.

    Please wait...z.bdatezpython b.pyZ13z=

    You Choosed Change Nickname Option.

    Please wait...z.nickzpython n.pyZ14z=

    You Choosed Chek Shout List Option.

    Please wait...z.updatezpython shout.pyZ15zG

    You Choosed Chek Latest Update in App Option.

    Please wait...zpython updateApp.pyZ16Z17Z18Z19Z20z=

    You Choosed Show Block List Option.

    Please wait...z	.blocked zpython showBlk.pyz
     Please Enter Valid Value�   )r   r   �str�input�cyan�yellowr   r   r   r   r   �print�red)Zchosser	   r	   r
   �main9   sh  













































































































 ��r(   )r   Zasyncior   r   Zrequestsr   ZblueZ	lightbluer'   Zwhiter%   Zgreenr$   �endZpurpler   r   r   r(   �KeyboardInterrupt�exitr	   r	   r	   r
   �<module>   s:   


 R�