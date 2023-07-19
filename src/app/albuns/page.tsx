import Header from "@/components/header/Header"
import Album_left_nav_bar from "@/components/left_nav_bar/album_left_nav_bar/page"
import Album_chooose from "@/components/album_components/album_home_alum_selection/page"
import style from './style.module.css'
import "../../../styles/globals.css"

export default function Home() {
  return (
    <body>
      <Header/>
      <div className={style.main}>
        <Album_left_nav_bar/>
        <div className={style.main_content}>
          <Album_chooose/>
          <Album_chooose/>
          <Album_chooose/>
          <Album_chooose/>
          <Album_chooose/>
          <Album_chooose/>
          <Album_chooose/>
        </div>
      </div>
    </body>
  )
}
