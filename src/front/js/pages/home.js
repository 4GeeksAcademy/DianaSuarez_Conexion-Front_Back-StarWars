import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext";
import { CardPeople } from "../component/cardpeople";
import { useNavigate } from "react-router-dom";
import swal from 'sweetalert';
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const navigate = useNavigate();

	useEffect(() => {
		actions.getPeoples();
	}, []);

	return (
		<>
			<div className="mt-5 d-flex justify-content-center text-center fs-4 text-dark-80">
				<p><strong>full stack developer</strong></p>
			</div>
			<div className="footer-view text-danger people mb-5 mt-2 justify-content-center bg-light">
				<div className="container">
					<div className="row text-dark d-flex justify-content-center gap-4">
						{store.people.map((people) => {
							return (
								<CardPeople people={people} key={people.id} />
							)
						})
						}
					</div>
				</div>
			</div>
		</>
	);
};

