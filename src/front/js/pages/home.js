import React from "react";
import "../../styles/home.css";
import homeImage from "../../img/Home1.png";

export const Home = () => {

	return (
		<>
			<div className="mt-5 d-flex justify-content-center text-center fs-4 text-dark-80">
			<div className="w-450 ms-5 mx-5 rounded">
				<img src={homeImage} />
				</div>
			</div>
			<div className="footer-view mb-5 mt-2 justify-content-center bg-light">
			</div>
		</>
	);
}