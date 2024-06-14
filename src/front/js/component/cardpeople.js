import React, {useState, useContext, useEffect} from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext.js";

export const CardPeople = ({ people }) => {
    const { store, actions } = useContext(Context);
    const token = localStorage.getItem("token");

    return (
        <div className="people card col-md-4" style={{ width: "22rem", height: "27rem" }}>
            <div>
                <a className="cardpeople" href="#">
                    <img className="img1" src={people.url_img1} style={{width: "100%", objectFit: "cover", height: "12rem"}} />
                </a>
            </div>
            <div className="card-body ms-2 p-2">
                <h3 className="card-title mt-2 mb-4 text-success"><strong>Full Stack Developer</strong></h3>
            </div>
        </div>
    )
};