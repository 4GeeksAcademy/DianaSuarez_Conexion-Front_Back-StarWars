import React, { useEffect, useState, useContext } from "react";
import { useParams } from 'react-router-dom';
import { Context } from "../store/appContext.js";

export const DetailPeople = () => {

    const params = useParams()
    console.log(params);
    // const { store, actions } = useContext(Context)
    const { store, actions } = useContext(Context);

    useEffect(() => {
        actions.getPeopleDetails(params.uid)
    }, [])

    return (
        <>
            <div className="jumbotron d-flex m-5 p-5 mw-100">
                <div className="tittle-top d-flex mx-auto">
                    <img src="https://productroulette.com/_nuxt/img/blog1.d1e9eb0.jpg" className="img-left mw-100 img-fluid" alt="..." />
                </div>
                <div className="container d-block text-center">
                    <h1 className="m-auto p-auto px-5">{store.people?.properties?.name}</h1>
                    <p className="lead mt-3 pt-3 px-5">Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,
                        totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo nemo enim ipsam.</p>
                </div>
            </div>
            <div>
                <p className="container d-block text-center text-danger border-bottom border-danger mt-2 ms-5 ps-5 mw-100"></p>
            </div>
            <div className="container d-flex justify-content-center text-danger">
                <h4 className="card-title w-2 px-5">Name <br /><br /> {store.people?.properties?.name}</h4>
                <h4 className="card-text w-2 m-2 px-5">Birth Year <br /><br /> {store.people?.properties?.birth_year}</h4>
                <h4 className="card-text w-2 m-2 px-5">Eye Color <br /><br /> {store.people?.properties?.gender}</h4>
                <h4 className="card-text w-2 m-2 px-5">Hair Color <br /><br /> {store.people?.properties?.height}</h4>
                <h4 className="card-text w-2 m-2 px-5"> <br /><br /> {store.people?.properties?.eye_color}</h4>
            </div>
        </>
    )
};




