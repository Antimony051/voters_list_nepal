import script
import json

state="1"       # the state whoose data you are currently downloading

stuck=["2", "5014", "13", "4435"]       # sometimes the connection gets lost and we need to pick up from where we left district,vdc,ward,pool info is stored to do that
done=0                                  # this is just for sanity check and is only required if the connection gets lost

flag=False
c=0

json_structure=open(f"/path/to/json/file/containing/the/required/ids/state{state}.json","rb")
get_id=json.load(json_structure)
json_structure.close()

out_file=open(f"/path/to/some/folder/name_state{state}.json","a")

print("processing state",state,"\n*************\n")
for district in get_id[state]:
    print("processing district",district)
    for vdc in get_id[state][district]:
        for ward in get_id[state][district][vdc]:
            for pool in get_id[state][district][vdc][ward]:
                c+=1
                if flag:
                    print("started download",pool)
                    out_file.write(script.final_request(state,district,vdc,ward,pool))
                elif pool==stuck[4]:        # just keep looping through the json structure until we hit the pool where we got stuck last time
                    flag=True
                    if c==done:             # if the downloading had completed before getting stuck continue
                        continue
                    elif c-1==done:         # if the last pool had not been downloaded, download it
                        print("started download",pool)
                        out_file.write(script.final_request(state,district,vdc,ward,pool))
                        print(pool,end=" ")
                    else:                   # if something is wrong this should catch it
                        print(f"trouble!\n according to previous logs we should have finished {c} requests\nbut only {done} were found in output file")
                        out_file.close()
                        exit()

out_file.close()
print("finished state",state)
