import React, { useState } from "react";
import classes from "./GeoCalc.module.css";
import { Button, InputAdornment, TextField } from "@mui/material";
import { Link } from "react-router-dom";
import { clearCredentials } from "../../http/auth";
import axiosInstance from "../../http/axios-instance";

const GeoCalc = () => {
  const [startLocation, setStartLocation] = useState<string>("");
  const [endLocation, setEndLocation] = useState<string>("");
  const [calculatedDistance, setCalculatedDistance] = useState<string>("");

  const handleCalculation = async () => {
    if (!startLocation || !endLocation) {
      alert("Please enter both start and end locations");
      return;
    }

    const params = {
      start_location: startLocation,
      destination_location: endLocation,
    };

    try {
      const response = await axiosInstance.get("/api/calc-distance", {
        params: params,
      });

      const data = response.data;
      setStartLocation(data.start_location.formatted_address);
      setEndLocation(data.destination_location.formatted_address);
      setCalculatedDistance(response.data.distance);
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className={classes.container}>
      <div className={classes.appContainer}>
        <div className={classes.innerBox}>
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: "16px",
            }}
          >
            <span className={classes.signInTextGray}>Calculate Distance</span>
          </div>
          <div>
            <div className={classes.formContainer}>
              <div className={classes.floatingCol}>
                <TextField
                  id="username"
                  name="username"
                  className={classes.floatingText}
                  value={startLocation}
                  placeholder="Enter Start Location"
                  onChange={(e) => {
                    setStartLocation(e.target.value);
                    setCalculatedDistance("");
                  }}
                  required
                />
              </div>
              <div className={classes.floatingCol}>
                <TextField
                  id="password"
                  name="password"
                  className={classes.floatingText}
                  placeholder="Enter Destination Location"
                  value={endLocation}
                  onChange={(e) => {
                    setEndLocation(e.target.value);
                    setCalculatedDistance("");
                  }}
                  required
                />
              </div>
            </div>
            {calculatedDistance && (
              <div className={classes.caclulatedDistanceText}>
                Calculated Geometrical Distance: {calculatedDistance} km
              </div>
            )}
            <Button
              className={classes.buttonText}
              sx={{
                borderColor: "#01337C",
                border: "1px solid",
                width: "95%",
                "&:hover": {
                  backgroundColor: "#01337C",
                },
                "&:active": {
                  backgroundColor: "#01337C",
                },
              }}
              type="submit"
              onClick={handleCalculation}
            >
              Calculate Distance
            </Button>
            <div className={classes.registerText}>
              <Link
                className={classes.link}
                onClick={() => {
                  clearCredentials();
                }}
                to={"/login"}
              >
                Logout User
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default GeoCalc;
