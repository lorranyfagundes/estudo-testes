describe ('Testando fomulários e campos', ()=>{
    it('deve preencher os campos da identificação com sucesso', ()=> {
        cy.visit('https://cac-tat.s3.eu-central-1.amazonaws.com/index.html');
        cy.get('#firstName').type('Lorrany');
        cy.get('#lastName').type('Fagundes');
        cy.get("#email").type('lorrany@email.com');
        cy.get('#open-text-area').type('testando por aqui');
        cy.get('.button').click();
        cy.get('.success').should('be.visible');
    });
});
;