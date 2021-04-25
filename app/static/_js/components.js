class Header extends HTMLElement {
    constructor() {
      super();
    }
    connectedCallback() {
        this.innerHTML = `
            <style>
            .g_container {
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
            }
            
            .g_header_container {
                width: 100%;
                height: calc(60px - 2px);
                position: fixed;
                background-color: var(--bkg-color);
                border-bottom: 3px solid var(--mint);
                z-index: 3;
            }
            
            .g_header_inner {
                padding: 10px 17px;
                width: calc(100% - 34px);
                height: calc(100% - 20px);
                display: flex;
                align-items: center;
            }

            .g_header_nav {
                display: flex;
            }

            .g_header_nav ul {
                list-style-type: none;

            }

            .nav_item {
                float: left;
                font-size: 15px;
                padding-right: 30px;
                font-family: 'Rubik';
            }

            .nav_item a {
                color: var(--text-color);
            }

            </style>
            <div class="g_header_container">
                <div class="g_header_inner">
                    <a href="/">
                        <div class="g_header_logo"><div id="logo_start">COIN</div><div id="logo_end">RAF</div></div>
                    </a>
                    <div class="g_header_nav">
                        <ul>
                            <li class='nav_item'>
                                <a id="nav_1" href='/crypto'>
                                    Crypto
                                </a>
                            </li>
                            <li class='nav_item'>
                                <a id="nav_2" href='/exchanges'>
                                    Exchanges
                                </a>
                            </li>
                            <li class='nav_item'>
                                <a id="nav_3" href='/discover'>
                                    Discover
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div class="color_mode_desktop">
                        <img src='/static/_images/_icons/moon.svg' style='width: 25px; height: 25px;'>
                    </div>
                    <div id="menu_icon" onclick='showMenu()'>
                        <img src='/static/_images/_icons/menu_icon.png' style='width: 25px; height: 25px; display: none;'>
                    </div>
                </div>
            </div>
        `;
      }
  }

customElements.define('g-header-component', Header);

class MobileMenu extends HTMLElement {
    constructor() {
      super();
    }
    connectedCallback() {
        this.innerHTML = `
            <style>

                #m_container {
                    width: 100vw;
                    height: 100vh;
                    background-color: var(--bkg-color);
                    position: absolute;
                    z-index: 4;
                    left: -500px;
                }

                #m_close_icon {
                    float: right;
                    padding-top: 8px;
                }

                .m_open_ani {
                    -webkit-animation: slide_open forwards;
                    animation: slide_open 0.5s forwards;
                }

                .m_close_ani {
                    -webkit-animation: slide_close forwards;
                    animation: slide_close 0.5s forwards;
                }

                .m_top {
                    padding: 10px 21px 25px 17px;
                }

                @-webkit-keyframes slide_open {
                    100% { left: 0; }
                }
                
                @keyframes slide_open {
                    100% { left: 0; }
                }

                @keyframes slide_close {
                    100% { left: -500px; }
                }

                @-webkit-keyframes slide_close {
                    100% { left: -500px; }
                }

                .m_dropdown_container {
                    font-family: 'Rubik';
                }

                .m_dropdown {
                    cursor: pointer;
                    padding: 18px;
                    width: 100%;
                    border: none;
                    text-align: left;
                    background-color: var(--bkg-color);
                    outline: none;
                    color: var(--text-color);
                    font-size: 15px;
                    transition: 0.4s;
                  }

                  .m_dropdown:after {
                    content: '\\002B';
                    color: var(--mint);
                    font-weight: bold;
                    float: right;
                    margin-left: 5px;
                    padding-right: 11px;
                  }

                  .active:after {
                    content: "\\2212";
                  }
                  
                  .active, .m_dropdown:hover {
                    color: var(--mint);
                  }
                  
                  .m_sub {
                    padding: 0 18px;
                    max-height: 0;
                    overflow: hidden;
                    transition: max-height 0.2s ease-out;
                  }

                  .m_list_padding {
                      padding-top: 10px;
                  }

                  .m_list_item {
                    padding-bottom: 10px;
                  }

                  .m_item {
                    cursor: pointer;
                    padding: 18px;
                    width: calc(100% - 36px);
                    text-align: left;
                    background-color: var(--bkg-color);
                    color: var(--text-color);
                    font-size: 15px;
                  }

                  #color_mode_span {
                      padding-right: 15px;
                  }

                  #color_mode_span span {
                      display: none;
                  }

                  .color_mode_mobile {
                    filter: invert(74%) sepia(46%) saturate(2241%) hue-rotate(98deg) brightness(101%) contrast(108%);
                  }

                  #color_mode_span:after {
                    content: var(--mode-text);
                    color: #000;
                  }
                

            </style>
            <div id='m_container'>
                <div class='m_top'>
                    <div id='m_close_icon' onclick='hideMenu()'>
                        <img src='/static/_images/_icons/menu_close.png'  style='width: 25px; height: 25px;'>
                    </div>
                    <a href="/">
                        <div id="m_logo" class="g_header_logo"><div id="logo_start">COIN</div><div id="logo_end">RAF</div></div>
                    </a>
                </div>
                <div class='m_dropdown_container'>
                    <button class="m_dropdown">Cryptocurrency</button>
                    <div class="m_sub">
                        <ul class='m_list'>
                            <a href="/crypto">
                                <li class='m_list_item'>View All</li>
                            </a>
                            <a href="/crypto">
                                <li class='m_list_item m_list_padding'>Hot</li>
                            </a>
                            <a href="/crypto">
                                <li class='m_list_item m_list_padding'>Recently Added</li>
                            </a>
                        </ul>
                    </div>
                    
                    <button class="m_dropdown">Exchanges</button>
                    <div class="m_sub">
                        <ul class='m_list'>
                            <a href="/crypto">
                                <li class='m_list_item'>View all</li>
                            </a>
                        </ul>
                    </div>
                    
                    <button class="m_dropdown">Discover</button>
                    <div class="m_sub">
                        <ul class='m_list'>
                            <a href="/crypto">
                                <li class='m_list_item'>View all</li>
                            </a>
                        </ul>
                    </div>

                    <div class="m_item">
                        <div class="color_mode_mobile flex-center-vertical">
                            <div id='color_mode_span'></div><img src='/static/_images/_icons/moon.svg' style='width: 25px; height: 25px;'>
                        </div>
                    </div>
                    

                </div>
                
        `;
      }
  }

customElements.define('g-mobile-menu', MobileMenu);