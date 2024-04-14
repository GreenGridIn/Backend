# GreenGridIn Flask API

### API

- `POST /predict` - Predict the power consumption of a server based on the input data.

  - Request Body:

    ```json
    {
      "air_temperature": 10.926,
      "pressure": 0.979103,
      "wind_speed": 9.014
    }
    ```

  - Response:

    ```json
    {
      "power": 33.6881
    }
    ```
