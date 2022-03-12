def get_statistics(input_list):
    # Write your code here.
    tot_sum=sum(input_list)
    n=len(input_list)
    mean=float(tot_sum)/float(n)

    input_list=sorted(input_list)
    if n%2==0:
        median=float(input_list[(n-1)//2]+input_list[((n-1)//2)+1])/2.0
    else:
        median=input_list[n//2]

    counts={x:input_list.count(x) for x in set(input_list)}
    mode=max(counts.keys(),key=lambda x:counts[x])

    sample_variance=sum([(x-mean)**2/(n-1) for x in input_list])
    sample_standard_deviation = sample_variance**0.5

    temp=sample_standard_deviation/n**0.5
    mean_confidence_interval=[mean-1.96*temp,mean+1.96*temp]
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }
