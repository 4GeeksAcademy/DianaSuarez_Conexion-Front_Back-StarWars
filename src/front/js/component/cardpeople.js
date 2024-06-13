import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext.js";
import { Link } from "react-router-dom";
import "../../styles/home.css";

export const CardPeople = ({ card }) => {
    const { store, actions } = useContext(Context);
    const [details, setDetails] = useState({})
    const [favorito, setFavorito] = useState({})
    const [className, setClassName] = useState("btn btn-outline-warning")

    useEffect(() => {
        fetch("https://www.swapi.tech/api/people/" + card.uid, {
            method: 'GET'
        })
            .then(res => res.json())
            .then(data => setDetails(data.result.properties))
            .catch(err => console.error(err));
    }, [])

    function onClickFavorito() {
        actions.addFavorite(card.name);
    }
    
    return (
        <div className="card col-3" style={{ width: "18rem" }}>
            <div className="card">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHiNvdbw8vVSnZ0AGw-AyiG85_10C2NRkzjPO9XZ9B3A&s"
                    className="card-img-top img-fluid w-250 h-150" alt="..." />
                <div className="card-body">
                    <h5 className="card-title mb-4">{card.name}</h5>
                    <p className="card-text mb-1">Gender: {details.gender}</p>
                    <p className="card-text mb-1">Hair color: {details.hair_color}</p>
                    <p className="card-text">Eye color: {details.eye_color}</p>
                    {/* Este es el boton que me lleva a la card individual */}
                </div>
                <div className="d-flex justify-content-between mb-4 m-3">
                    <Link to={`/detailpeople/${card.uid}`}>
                        <button className="btn btn-outline-primary" type="button">Learn more!</button>
                    </Link>
                    {/* <a href="#" className={`btn btn-outline-warning ${store.favorites.includes(card.name) ? "active" : ""}`}>
                        <i className="fa-regular fa-heart" onClick={onClickFavorito} ></i>
                    </a> */}
                </div>
            </div>
        </div>
    )
};
