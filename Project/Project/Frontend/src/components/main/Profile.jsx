import Image from "react-bootstrap/Image";
import React from "react";
import './Profile.css'

export default function Profile(){
    return(
        <section className="main">
            <div className="left">
                <div className="left-img">
                        <Image
                            src="https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1171&q=80"
                            roundedCircle
                        />
                </div>
                <div className="left-text">
                    <h3>Elizabeth Clover</h3>
                </div>
                <div className="left-btn">
                    <button>Share profile</button>
                </div>
            </div>
            <div className="right">
                <div class="skill cont">
                <div>
                    <div class="s-cont">
                        <div>
                            <h1 class="txt">OverAll Score : </h1>
                        </div>
                    </div>
                    <div class="skill-list skill-open">
                        <div class="s-data">
                            <div class="s-head">
                                <h3 class="s-name">S - Scientific</h3>
                                <span class="s-number">80%</span>
                            </div>
                            <div class="s-bar">
                                <div class="s-per s-s">
                                    <span class="s-per s-s"></span>
                                </div>
                            </div>
                        </div>

                        <div class="s-data">
                            <div class="s-head">
                                <h3 class="s-name">T - Technical</h3>
                                <span class="s-number">60%</span>
                            </div>
                            <div class="s-bar">
                                <div class="s-per s-t">
                                    <span class="s-per s-t"></span>
                                </div>
                            </div>
                        </div>

                        <div class="s-data">
                            <div class="s-head">
                                <h3 class="s-name">E - Engineering</h3>
                                <span class="s-number">70%</span>
                            </div>
                            <div class="s-bar s-l">
                                <div class="s-per s-e">
                                    <span class="s-per s-e"></span>
                                </div>
                            </div>

                        </div>

                        <div class="s-data">
                            <div class="s-head">
                                <h3 class="s-name">M - Maths</h3>
                                <span class="s-number">60%</span>
                            </div>
                            <div class="s-bar s-l">
                                <div class="s-per s-m">
                                    <span class="s-per s-m"></span>
                                </div>
                            </div>

                        </div>

                    </div>
                </div>
                </div>
                <div className="rit-tot">
                    <h3>Total Score : </h3>
                </div>
                <div class="circle-wrap">
                    <div class="circle">
                    <div class="mask full">
                        <div class="fill"></div>
                    </div>
                    <div class="mask half">
                        <div class="fill"></div>
                    </div>
                    <div class="inside-circle"> 67.5% </div>
                    </div>
                </div>
            </div>
        </section>
    )
}