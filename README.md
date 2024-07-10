<div align= >

# Anomaly-Detection


</div>
<div align="center">
   <img align="center" height="350px"  src="images/python_anomaly_detection_isolation_forest.gif" alt="logo">
   <br>


</div>

<p align="center">
    <br>
</p>

## <img align="center"  height =50px src="https://user-images.githubusercontent.com/71986226/154076110-1233d7a8-92c2-4d79-82c1-30e278aa518a.gif"> Overview

<ul>
<li> Built using <a href="https://docs.python.org/3/">Python</a>.</li>
<li> This is a solution for Anomaly Detection Problem</li>
<li> This Project simulates real-time sequences of floating-point numbers, that could represent various metrics such as financial transactions or system metrics.</li>

<br>

</ul>
</li>
</ul>
<a id = "Started"></a>

## <img  align= center width=50px height=50px src="https://c.tenor.com/HgX89Yku5V4AAAAi/to-the-moon.gif"> How To Run

- First install the <a href="https://github.com/nouralmulhem/Cipher-Sphere/blob/main/requirements.txt">needed packages</a>.</li>

```sh
pip install -r requirements.txt
```

- Folder Structure

```sh
├─── images
├─── src
│   ├── model
│     └─── autoencoder_model.h5
│   ├── RNN
│     ├── RNN.ipynb
│     └─── utile.py
│   ├── AnomalyDetection.py
│   ├── Hotelling.py
│   └─── Streaming.py
....
```

<br/>

## Anomaly Detection Script

This script allows you to run different anomaly detection algorithms on your data.

### Available Algorithms

- `hotelling`: Hotelling's T-squared algorithm for multivariate anomaly detection.
- `ocsvm`: One-Class Support Vector Machine for anomaly detection.
- `variance`: Variance-based anomaly detection.
- `isolated_forest`: Isolation Forest algorithm for anomaly detection.

### Usage

To run the script, use the following command:

```sh
python path/to/AnomalyDetection.py --algo <algorithm> [--plot]
```

- `--algo <algorithm>`: Choose the algorithm to run. Options are `hotelling`, `ocsvm`, `variance`, and `isolated_forest`.
- `--plot`: (Optional) Set this flag to plot the results.

<br/>

## Streaming Script

This script allows you to run and stream the data and detect anomalies on the fly from generated data


### Usage

To run the script, use the following command:

```sh
python path/to/Streaming.py 
```
OR
```sh
python path/to/StreamingV2.py 
```

<br/>

<hr style="background-color: #4b4c60"></hr>

<a id ="References"></a>

## <img  align="center" width= 40px height =55px src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnI2ZGR1dXVnM2VpdGpzZ3pydWJwYTF4cTVzYmppdGFiNGsyNmJ2cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Z5HWPHECnylZeYOZ6U/giphy.gif"> References


| Name       | Link                                                                 |
|-----------------|--------------------------------------------------------------------------|
| ` Adversarially Learned Anomaly Detection`     | [Link](https://arxiv.org/abs/1812.02288) |
| `How to use Python for anomaly detection in data: Detailed Steps`         | [Link](https://dataheadhunters.com/academy/how-to-use-python-for-anomaly-detection-in-data-detailed-steps/) |
| `Anomaly Detection`      | [Link](https://avinetworks.com/glossary/anomaly-detection/#:~:text=Anomaly%20detection%20is%20the%20identification,noise%2C%20novelties%2C%20and%20exceptions.) |

<br/>
<hr style="background-color: #4b4c60"></hr>
<a id ="Contributors"></a>

## <img  align="center" width= 70px height =55px src="https://media0.giphy.com/media/Xy702eMOiGGPzk4Zkd/giphy.gif?cid=ecf05e475vmf48k83bvzye3w2m2xl03iyem3tkuw2krpkb7k&rid=giphy.gif&ct=s"> Contributors

<table >
  <tr>
    <td align="center"><a href="https://github.com/nouralmulhem"><img src="https://avatars.githubusercontent.com/u/76218033?v=4" width="150;" alt=""/><br /><sub><b>Nour Almulhem</b></sub></a><br /></td>
  </tr>
</table>

<a id ="License"></a>

## 🔒 License

> **Note**: This software is licensed under MIT License, See [License](https://github.com/nouralmulhem/Cipher-Sphere/blob/main/LICENSE) for more information ©nouralmulhem.
