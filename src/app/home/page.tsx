import Header from "@/components/header/Header"
import Home_left_nav_bar from "@/components/left_nav_bar/Home_left_nav_bar/page"
import Drive_conection from "@/components/home_maincontent/page"
import Em_andamento from "@/components/home_maincontent/em-andamento/page"
import Concluidos from "@/components/home_maincontent/concluido/page"
import style from './style.module.css'
import "../../../styles/globals.css"

export default function Home() {
  return (
    <body>
      <Header/>
      <div className={style.main}>
        <Home_left_nav_bar/>

        <div className={style.main_content}>
          <Drive_conection/>

          <div className={style.andamento_concluidos}>
            <Em_andamento/>
            <Concluidos/>
          </div>
        </div>
        
      </div>
    </body>
  )
}
