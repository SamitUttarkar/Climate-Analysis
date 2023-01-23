![🌏_Climate_Analysis](https://user-images.githubusercontent.com/67644483/214052529-ebde7c12-bdb0-468c-96b1-cc424c2f28e5.png)


# Project Breif
Visualisation of  daily stream gauge measurements (which provide a sort of spatially and temporally averaged rainfall record) from the London Road gauge on Manchester's river Medlock. It's in Longsight and is station 69020 in the UK's National River Flow Archive (NRFA).

# Project Results:-



#### **This graph visualises the flow rate's frequency. It is observed in the original scale that the graph is very Right skewed. Therefore we take the log of flow rate to visualise it better**

<img width="786" alt="Screenshot 2023-01-23 at 1 36 10 PM" src="https://user-images.githubusercontent.com/67644483/214052982-e1eb179f-70c4-44d1-b85d-8a063981f25a.png">



#### **As we can observe the flow rate is quite constant over the period of time.There are rare instances of extremes, such as around January 1, 1974, when we can see the flow rate reaching an all-time low, which makes it stand out**

<img width="789" alt="Screenshot 2023-01-23 at 1 38 14 PM" src="https://user-images.githubusercontent.com/67644483/214053408-e8c8d5a4-abc6-4b32-b71a-1537f79f156d.png">



#### **The flow rate seems to be in a parabola shape facing upwards but the change is not considerable.**

<img width="806" alt="Screenshot 2023-01-23 at 1 41 07 PM" src="https://user-images.githubusercontent.com/67644483/214053983-895869e0-fbcb-4255-b6b0-4ef3b09afe1e.png">



## Next we plot the same visualisation for median and quantile range and observe how it varies are time passes

#### **Here we can clearly observe that the shape of the graph is polynomial. Thus making our results visualise better**

<img width="799" alt="Screenshot 2023-01-23 at 1 42 39 PM" src="https://user-images.githubusercontent.com/67644483/214054331-8950e856-6654-4c4b-8649-b6721cf71b21.png">



## Next we Plot heat map

<img width="799" alt="Screenshot 2023-01-23 at 1 43 46 PM" src="https://user-images.githubusercontent.com/67644483/214054567-59585667-444c-4f3d-b61f-093f6e76f0e7.png">

## Libraries Usef for this project
- numpy
- scipy
- datetime
- pandas
- matplotlib


