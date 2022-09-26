
high_throughput_cm = {
    "roundabout" : 50,
    "stop_sign" : 20,
    "traffic_lights" : 90
}

medium_throughput_cm = {
    "roundabout" : 75,
    "stop_sign" : 30,
    "traffic_lights" : 75
}

low_throughput_cm = {
    "roundabout" : 90,
    "stop_sign" : 40,
    "traffic_lights" : 30
}

def control_method_for_cpm(cpm:float):
    cm_score = []
    if cpm >= 20:
        for x in high_throughput_cm:
            if high_throughput_cm[x] == max(high_throughput_cm.values()):
                cm_score.append(x)
        return (f"The best control method: {list(cm_score)} with efficiency of: {high_throughput_cm[cm_score[0]]}%.")
    elif cpm <20 and cpm >=10:
        for x in medium_throughput_cm:
            if medium_throughput_cm[x] == max(medium_throughput_cm.values()):
                cm_score.append(x)
        return (f"The best control method: {list(cm_score)} with efficiency of: {medium_throughput_cm[cm_score[0]]}%.")
    else:
        for x in low_throughput_cm:
            if low_throughput_cm[x] == max(low_throughput_cm.values()):
                cm_score.append(x)
        return (f"The best control method: {list(cm_score)} with efficiency of: {low_throughput_cm[cm_score[0]]}%.")
    

road1_input = input("Enter Road 1's CPM: ")
print(control_method_for_cpm (float(road1_input)))

road2_input = input("Enter Road 2's CPM: ")
print(control_method_for_cpm (float(road2_input)))

road3_input = input("Enter Road 3's CPM: ")
print(control_method_for_cpm (float(road3_input)))

road4_input = input("Enter Road 4's CPM: ")
print(control_method_for_cpm (float(road4_input)))