o
    >��bA  �                   @   s�   d dl Z d dlZd dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZ	dZ
dZdZd	Zd
ZdZe �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  ey`   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35mz

 https://bit.ly/3Hz6Ff5�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )Nz..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �follower.py�header"   s   


r   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint)   s
   
�r   c                  C   sZ  d} 	 t �d� ttd t �}|dk�r�d| d }dd	lm} |� }d
|d< d|d< d|d< d|d< z
tj| ||d�}W n   t	t
d � t��  Y |�� d d }t �d� t�  t	td � t�d� t �d� t�  t	td t | � t	td t |�� d d  d � t�d� d}g }|�� d d }tt|��D ]K}zDt	td t |�� d d | d  t d t d  |�� d d | d!  � |�� d d | d }	t�d"� |�|	� |d#7 }W q�   Y q�	 tttd$ ��}
|
�� }|d%k�r�t �d� t�  t �d� tttd& t ��}t�d'� t �d� t�  ttd( � t�d� t �d� t�  |D ]j}d}d)| }dd	lm} |� }||d< d|d< d|d< d|d< d*|d+< ztj|||d�}t�d'� W n
   t	t
d, � Y t�d-� |�� d. }|d/k�r�t	td0 t | � �q:t	td1 | d2 t | � �q:q�t	t
d3 � q)4Nz5https://circle.robi.com.bd/mylife/appapi/appcall.php?Tzlolcat clean2.shz
     Enter Circle ID: � z)op=getFollowerInfoList&offset=0&nickname=z
&limit=100r   )�CaseInsensitiveDictZ d29ac47b3ce9de73bb99c1b98dd6159bz	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Type)�headers�dataz
     Errorr   Zfollowerr   z$

     Your Follower Data Loading...�   z
     Your ID: z
     Total Followers: �totalr	   z
 Nickname: Znicknamez
  Number: �+Zmsisdng�������?�   z-
 Are you sure clean your follower list y/n? �yz     Enter Your API Key: �   z$

     Your Request In Prossesing...zop=blockUser&nickname=zcircle.robi.com.bdZHostz     No internetg      �?ZrdescZOKz&

      You have successfully blocked z

      � z
     Please Enter Valid ID)r   r   �input�green�yellowZrequests.structuresr   �requestsZpost�print�redr
   �exit�jsonr   r   r   �range�len�cyan�append�str�white�lowerr   �purpler   )Zm_url�userr   r   r   Zrequ_for_followerr   �x�idZnickZsure�sZapi�mZurlZrequZrespZenterr   r   r   �main0   s�   





$
P








	

 �7�r3   )r   r
   r%   r   r!   r   ZblueZ	lightbluer#   r+   r    r   r(   �endr-   Zmarkr   r   r3   �KeyboardInterruptr$   r   r   r   r   �<module>   s4    


p�