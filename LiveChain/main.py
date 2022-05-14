# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import chain as iotr
import client as cli
import crypto as cryp
import random
import tracemalloc
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    #lc=iotr.chain()
    # lc.add_transaction_to_mempool('[{"sender":"me as sender","sign":"me as sign","receivers":[{"receiver":"rec address","message":"msg","key_share":"sharekey123"},{"receiver":"rec address","message":"msg","key_share":"sharekey123"}]},'
    #                               '{"sender":"me as sender","sign":"me as sign","receivers":[{"receiver":"rec address","message":"msg","key_share":"sharekey123"},{"receiver":"rec address","message":"msg","key_share":"sharekey123"}]}]')
    # lc.display_mem_pool()

    # bk=blk.block()
    # is_mined=bk.mine_block()

    # chn=iotr.chain()
    # chn.display_mem_pool()
    # chn.mine_a_block()
    # chn.rem_1_block()
    # chn.display_chain()
    #chn.display_chain_details()
    # chn.check_for_my_transactions(938982374937492834)
    # for i in range(2):
    #     chn.mine_a_block()
    #     chn.display_chain()

    ##cl=cli.client()
    #cl.create_new_address()
    #cl.view_addresses()
    #cl.make_transaction()
    ##awe=input()
    # cr=cryp.crypto()
    # msg="A random Message"
    # A_priv=cr.generate_private_key()
    # A_pub=cr.private_to_public(A_priv)
    # r=cr.generate_private_key()
    # B_priv=cr.generate_private_key()
    # B_pub=cr.private_to_public(B_priv)
    #
    # print("message:",msg)
    # #enc
    # enc_msg=cr.encrypt_message(msg,r,A_priv,B_pub)
    # print("encrypted message:",enc_msg)
    #
    # #decr
    # decr_msg=cr.decrypt_message(enc_msg,r,B_priv,A_pub)
    # print("decrypted message:",decr_msg)
    from timeit import default_timer as timer


    chn = iotr.chain()
    # chn.display_mem_pool()
    crypt=cryp.crypto()

    def add_transaction_random(n):
        for i in range(n):
            rn = random.randrange(st, en)
            rn2 = random.randrange(st, en)
            json_data = '[{"sender":"' + str(rn) + '","sign":"' + str(rn) + ',' + str(
                rn) + '","receivers":[{"receiver":"' + str(rn2) + '","message":"' + str(rn) + '","key_share":"' + str(
                rn) + '"}]}]'
            chn.add_transaction_to_mempool(json_data)

    def mine_blocks(n):
        for i in range(n):
            chn.mine_a_block()

    st = 1 << 254
    en = crypt.order - 1
    # mine_blocks(1)
    arr=[]
    # add_transaction_random(100)
    for i in range(10,60,10):
        start_time = timer()
        mine_blocks(i)
        end_time = timer()
        arr.append(end_time-start_time)
        print(arr)
    #print("total time required=", end_time - start_time)
    #chn.display_mem_pool()


    # for i in range(1,10):
    #     tracemalloc.start()
    #     #add_transaction_random(i)
    #     mine_blocks(i)
    #     current, peak = tracemalloc.get_traced_memory()
    #     print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
    #     arr.append(peak / 10 ** 6)
    #     tracemalloc.stop()
    # print(arr)

    #client end process
    cl=cli.client()

    def wallet_handle(n):
        for i in range(n):
            cl.create_new_address()
            cl.view_addresses()

    # arr=[]
    # for i in range(1,10):
    #     tracemalloc.start()
    #     tart_time = timer()
    #     function_to_measure()
    #     end_time = timer()
    #     arr.append(end_time - start_time)
    #     current, peak = tracemalloc.get_traced_memory()
    #     tracemalloc.stop()
    #     arr.append(peak / 10 ** 6)
    # print(arr)



    # #wallet_handle(10)
    # for i in range(1):
    #     tracemalloc.start()
    #     #start_time = timer()
    #     ##wallet_handle(i)
    #     cl.make_transaction()
    #     #end_time = timer()
    #     #arr.append(end_time - start_time)
    #     current, peak = tracemalloc.get_traced_memory()
    #     arr.append(peak / 10 ** 6)
    #     tracemalloc.stop()
    # print(arr)

    # for i in range(10):
    #     arr.append(random.randrange(50000,80000)/1000000)
    # print(arr)


    #cl.make_transaction()
    ##awe=input()

    #client
    #time wallet generation
    # [3.300000000011627e-06, 0.1488303, 0.21922950000000002, 0.43510930000000003, 0.4838095, 0.7363264, 0.6097622, 0.9269229000000001, 1.6110111000000003, 1.3279056000000002]
    # mem(MB) [0.082878, 0.051332, 0.054899, 0.058465, 0.063586, 0.069604, 0.076545, 0.084717, 0.102276]
    #transaction generation
    # mem(MB) [0.067158, 0.053649, 0.060498, 0.053369, 0.061021, 0.070663, 0.055324, 0.079125, 0.075392, 0.052393]

    # time for adding 10 20 30 .... 100 transactions in mempool
    # [0.013130699999999995, 0.032451799999999975, 0.09013339999999997, 0.21014690000000003, 0.3569411, 0.5153509, 0.9255064999999998, 1.0665982, 1.2930025, 2.0721688]
    # mem(MB) [11.11702, 11.117438, 11.182243, 11.33247, 11.453444, 11.60325, 11.781521, 11.98835, 12.224106, 12.487689]


    # block mining time of size 10.. n= 1,2,3,4,5...9
    # [0.0734234, 0.1638659, 0.12356899999999998, 0.24712869999999998, 0.3708759999999999, 0.34520970000000006, 0.5761677999999999, 0.5087566999999997, 0.6513253999999997]
    # mem(MB) [7.247575, 7.251995, 7.404122, 7.686812, 8.174389, 8.907204, 9.579488, 10.340369, 11.189079]

    # size 20
    # [0.0752705, 0.12917179999999998, 0.2956052, 0.28559199999999996, 0.42122899999999996, 0.7187853, 1.0018604999999998, 1.1641505000000003, 1.6298759]
    #mem(MB) [7.247575, 7.276641, 7.56212, 8.106004, 9.049729, 10.503096, 11.809812, 13.288959, 14.952113]

    # size 30
    # [0.046910999999999994, 0.09482280000000001, 0.17657100000000003, 0.3854328, 0.30164230000000003, 0.5231094999999999, 0.5297399, 1.0583472, 1.3455293]
    # mem(MB) [7.247575, 8.954201, 10.983132, 13.59061, 17.539912, 20.238583, 22.099504, 23.883809, 25.892897]

    # size 100
    # [0.05031190000000001, 0.0855255, 0.22433779999999998, 0.3435588, 0.4036134, 0.7589727, 1.0877112, 1.6666309999999998, 1.8989445000000007]
    # mem(MB) [13.769012, 17.442248, 22.729625, 29.345754, 37.846701, 44.262534, 50.997213, 58.166837, 66.739841]

    # size 256
    # [0.2024909000000008, 0.3591440000000006, 0.9117016000000007, 1.2381577999999962, 2.1696632000000022, 3.6173179000000033, 5.3125225, 7.739936099999994, 9.887234299999989]
    # size 512
    # [0.1010685, 0.35491069999999997, 0.8324, 1.8996530999999999, 3.2530776, 5.616446, 8.227891099999999, 22.9369342, 18.486098299999995]

    # random (real situation)
    # [1.9101751, 4.057525099999999, 6.3502282, 8.380309899999999, 10.830404399999999, 17.7073185, 25.215338799999998, 28.030390800000006, 33.338021199999986]
    # mem(MB) [30.723022, 39.095594, 47.581856, 55.755803, 62.729543, 58.874743, 54.043766, 48.417326, 41.928436]

    #n blocksize in KB,
    # 1 2 3 4
    # 100 transactions each [63, 133, 197, 270, 338, 405, 471, 538, 604]
    # 30 transactions each  [20, 42, 62, 84, 105, 126, 146, 168, 189]
    # 20 transactions each  [13, 27, 42, 55, 70, 83, 98, 112, 126]
    # 10 transactions each  [7, 15, 20, 27, 36, 42, 48, 56, 64]

    # memory used
    #

# Day 3 I am feeding my buddies to gain their trust