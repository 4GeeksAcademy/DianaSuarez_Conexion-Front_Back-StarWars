import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext.js";
import { Link } from "react-router-dom";
import "../../styles/home.css";

export const CardPeople = ({ card }) => {

    return (
        <div className="card col-3" style={{ width: "18rem" }}>
            <div className="card">
                <img src="https://static.vecteezy.com/system/resources/previews/010/519/506/non_2x/hello-speech-bubbles-with-cartoon-character-free-vector.jpg"
                    className="card-img-top img-fluid w-250 h-150" alt="..." />
    
                {/* <div className="d-flex justify-content-between mb-4 m-3">
                    <Link to={`/detailpeople/${card.uid}`}>
                        <button className="btn btn-outline-primary" type="button">Learn more!</button>
                    </Link>
                </div> */}
            </div>
        </div>
    )
};
