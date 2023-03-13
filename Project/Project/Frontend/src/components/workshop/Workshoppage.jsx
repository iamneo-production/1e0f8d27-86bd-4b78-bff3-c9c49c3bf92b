import React from "react";
import image from "./img-4.jpg";
import "./workshoppage.css";
function Workshoppage() {
  const eventList = [
    {
      img: image,
      name: "Hack Orlando",
      link: "/eventdetails",
      descrip:
        "Hello, this is Catherine speaking, the creator of Hack Orlando. I loved meeting other people who are interested in coding, but I didn't love online meetings. Many of the hackathons and other programs I've been in have been completed online.",
      pay: 0,
      date: "20-04-2023",
      time: "10:00 AM",
      place: "Online"
    },
    {
      img: image,
      name: "Krypthon - Hackathon",
      link: "/eventdetails",
      descrip:
        "Krypthon is an exciting 36-hour hackathon that challenges participants to develop industry-ready solutions",
      pay: 0,
      date: "24-04-2023",
      time: "11:00 AM",
      place: "Online"
    },
    {
      img: image,
      name: "Accenture Hack Diva",
      link: "/eventdetails",
      descrip:
        "Accenture Hack Diva - a contest for women in engineering, is designed to empower and encourage female students to showcase their skills and win BIG. This contest is open to all female students from all engineering colleges in India who have graduated in 2022 or will be graduating in 2023.",
      pay: 0,
      date: "30-04-2023",
      time: "9:00 AM",
      place: "Kolkata, West Bengal, India"
    },
    {
      img: image,
      name: "Smart Bengal Hackathon 2023",
      link: "/eventdetails",
      descrip:
        "Smart Bengal Hackathon 2023 is a statewide initiative to provide students a platform to solve some of the pressing problems we face in our daily lives, and thus inculcate a culture of product innovation and a mindset of problem-solving.",
      pay: 0,
      date: "12-05-2023",
      time: "11:00 AM",
      place: "Delhi"
    }
  ];
  let i = 1;
  return (
    <>
      <center className="mt-0  p-3 m-5 rounded">
        <h1>Hackathons</h1>
      </center>
      {eventList.map((t) => {
        return (
          <a href={t.link} id="link">
            <div
              id="wrapper"
              className="d-flex mx-5 my-1 rounded border p-3 border-primary"
            >
              <div className="col-1 my-4 offset-1 rounded d-flex justify-content-center align-items-center">
                <h3>{i++}</h3>
              </div>
              <div className="col-2 my-4 mx-1  d-flex rounded justify-content-center align-items-center">
                <img
                  src={t.img}
                  style={{ width: "200px", height: "100px" }}
                ></img>
              </div>
              <div className="col-6 rounded d-flex border-left border-right border-info flex-column justify-content-center align-items-center">
                <div>
                  <h4>{t.name}</h4>
                </div>
                <p>{t.descrip}</p>
                <div className="">Rupees {t.pay} only</div>
              </div>
              <div className="col-3  my-4 mx-1 rounded ">
                <div className="d-flex mt-3 ml-3">
                  <i class="bi bi-calendar"></i>
                  <p className="ml-5">{t.date}</p>
                </div>
                <div className="d-flex ml-2">
                  <i class="bi bi-clock"></i>
                  <p className="ml-5">{t.time}</p>
                </div>
                <div className="d-flex ml-3">
                  <i class="bi bi-geo-alt"></i>
                  <p className="ml-5">{t.place}</p>
                </div>
              </div>
            </div>
          </a>
        );
      })}
    </>
  );
}

export default Workshoppage;
