import Header from "@/components/header/Header"
import style from './style.module.css'
import "../../../styles/globals.css"
import {FolderEdit, AtSign, Plus } from 'lucide-react'

export default function Create_album() {
  return (
    <body>
      <Header/>
      <div className={style.gradient}>

        <form className={style.form} action="">
          
          <div className={style.content}>
            <label className={style.image} htmlFor="image"></label>
            <input type="file" id="image" className={style.file_upload} src="" alt="" />

            <div className={style.forms}>
                <input className={style.title} name="title" type="text" placeholder="Escolha um nome..." />
                <textarea className={style.description} name="descricao" id="" cols="30" rows="10"placeholder="Adicione uma descrição ao álbum..."></textarea>

                <div className={style.info}>
                  <div className={style.aling}>
                    <FolderEdit color="white"/>
                    <p>get_author_identifier</p>
                  </div>

                  <div className={style.aling}>
                    <AtSign color="white"/>
                    <p>??? insta?</p>
                  </div>
                </div>
            </div>
          </div>

          <div className={style.mutiple_image_input}>
            
            <label className={style.mutiple_image_label} htmlFor="files">
              <Plus className={style.plus_icon} width={60} height={50} color='white'/>
            </label>
            <input className={style.mutiple_image} type="file" id="files" name="files" multiple/>

          </div>
        
        </form>       

      </div>

    </body>
  )
}
